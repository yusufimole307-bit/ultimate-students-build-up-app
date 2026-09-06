import streamlit as st

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="Ultimate Trivia Challenge",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for polished typography, padding, and smooth button styles
st.markdown(
    """
    <style>
    .main { padding-top: 2rem; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .question-box {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF4B4B;
        margin-bottom: 25px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 2. Game Data (Questions, Options, and Answers)
QUIZ_DATA = [
    {
        "question": "Which planet in our solar system is known for its spectacular ring system?",
        "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
        "answer": "Saturn",
    },
    {
        "question": "What is the rarest naturally occurring element on Earth?",
        "options": ["Astatine", "Francium", "Oganesson", "Uranium"],
        "answer": "Astatine",
    },
    {
        "question": "Which programmer-focused movie features the line, 'Welcome to the desert of the real'?",
        "options": ["The Matrix", "Tron", "Inception", "Ex Machina"],
        "answer": "The Matrix",
    },
    {
        "question": "What does the 'S' stand for in the popular SOLID design principles?",
        "options": [
            "Single-responsibility",
            "Scope-isolation",
            "Structural-pattern",
            "State-management",
        ],
        "answer": "Single-responsibility",
    },
    {
        "question": "In what year was the Python programming language first released by Guido van Rossum?",
        "options": ["1989", "1991", "1995", "2000"],
        "answer": "1991",
    },
]

# 3. Session State Initialization
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_complete" not in st.session_state:
    st.session_state.quiz_complete = False
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None
if "answered" not in st.session_state:
    st.session_state.answered = False


# 4. Helper Functions for App Control
def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_complete = False
    st.session_state.selected_option = None
    st.session_state.answered = False


def next_question():
    st.session_state.current_question += 1
    st.session_state.selected_option = None
    st.session_state.answered = False
    if st.session_state.current_question >= len(QUIZ_DATA):
        st.session_state.quiz_complete = True


# 5. Main Game Layout
st.title("🏆 Ultimate Trivia Challenge")
st.write("Test your knowledge and see if you can score a perfect 5/5!")
st.divider()

# Game Over Screen
if st.session_state.quiz_complete:
    st.balloons()
    st.success("🎉 You have finished the quiz!")

    # Dynamic feedback based on performance
    final_score = st.session_state.score
    total_q = len(QUIZ_DATA)

    st.metric(label="Your Final Score", value=f"{final_score} / {total_q}")

    if final_score == total_q:
        st.subheader("🥇 Perfect Score! You are a master triviologist!")
    elif final_score >= total_q // 2:
        st.subheader("🥈 Good job! Solid effort.")
    else:
        st.subheader("🥉 Keep practicing! Try reading up and give it another go.")

    if st.button("🔄 Play Again", type="primary"):
        reset_quiz()
        st.rerun()

# Active Question Screen
else:
    current_idx = st.session_state.current_question
    q_data = QUIZ_DATA[current_idx]

    # Progress Indicator
    st.write(f"**Question {current_idx + 1} of {len(QUIZ_DATA)}**")
    st.progress((current_idx) / len(QUIZ_DATA))

    # Question Display Box
    st.markdown(
        f'<div class="question-box"><h3>{q_data["question"]}</h3></div>',
        unsafe_allow_html=True,
    )

    # Display options as single-choice radio buttons
    # Form layout forces users to explicitly click a verification button
    with st.form(key=f"question_form_{current_idx}"):
        choice = st.radio(
            "Choose the correct answer:",
            options=q_data["options"],
            index=None,
            key=f"radio_{current_idx}",
            label_visibility="collapsed",
        )

        submit_btn = st.form_submit_button(
            label="Submit Answer", use_container_width=True
        )

        if submit_btn:
            if choice is None:
                st.warning("Please select an option before submitting!")
            else:
                st.session_state.selected_option = choice
                st.session_state.answered = True

    # Show Answer Evaluation after submission
    if st.session_state.answered:
        user_choice = st.session_state.selected_option
        correct_choice = q_data["answer"]

        if user_choice == correct_choice:
            st.success(f"🎯 **Correct!** Excellent choice.")
            # Safeguard scoring context inside unique states so it updates exactly once per question
            if f"scored_{current_idx}" not in st.session_state:
                st.session_state.score += 1
                st.session_state[f"scored_{current_idx}"] = True
        else:
            st.error(f"❌ **Incorrect.** The correct answer was: **{correct_choice}**")

        # Next button moves out of the form block for safe flow control
        st.button("Next Question ➡️", on_click=next_question, type="primary")

    # Score tracker sidebar footprint
    with st.sidebar:
        st.header("🏆 Live Stats")
        st.metric(label="Current Score", value=st.session_state.score)
        if st.button("Reset Game"):
            reset_quiz()
            st.rerun()



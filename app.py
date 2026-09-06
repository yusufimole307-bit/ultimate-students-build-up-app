import random
import time
import streamlit as st

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="Ultimate Trivia Challenge",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for polished typography and UI wrappers
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

# 2. Expansive Master Question Pool
MASTER_QUIZ_POOL = [
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
    {
        "question": "Which protocol is primarily used to securely transfer files over the web?",
        "options": ["SFTP", "HTTP", "SMTP", "IMAP"],
        "answer": "SFTP",
    },
    {
        "question": "What is the computational time complexity of searching a sorted array using Binary Search?",
        "options": ["O(log n)", "O(n)", "O(n log n)", "O(1)"],
        "answer": "O(log n)",
    },
    {
        "question": "Which SQL keyword is used to sort the result-set in descending or ascending order?",
        "options": ["ORDER BY", "SORT BY", "GROUP BY", "ALIGN BY"],
        "answer": "ORDER BY",
    },
    {
        "question": "In Git version control, which command combines multiple branches back into one tracking branch?",
        "options": ["merge", "push", "commit", "fork"],
        "answer": "merge",
    },
    {
        "question": "What is the main component of a standard computer processing setup responsible for long-term data persistence?",
        "options": ["SSD / HDD", "RAM", "CPU Cache", "GPU vRAM"],
        "answer": "SSD / HDD",
    },
]

# Strategic Configuration
QUESTIONS_PER_GAME = 5
SECONDS_PER_QUESTION = 15


# 3. Session State Initialization Logic
def initialize_game():
    # Randomly select a subset of questions from our master pool
    selected_questions = random.sample(MASTER_QUIZ_POOL, QUESTIONS_PER_GAME)

    # Shuffle the options for each selected question so option order changes
    for q in selected_questions:
        # Create a copy so we don't accidentally modify the master list structurally
        q["options"] = list(q["options"])
        random.shuffle(q["options"])

    st.session_state.active_questions = selected_questions
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_complete = False
    st.session_state.selected_option = None
    st.session_state.answered = False
    st.session_state.start_time = time.time()  # Track time for current question


if "active_questions" not in st.session_state:
    initialize_game()


def reset_quiz():
    initialize_game()


def next_question():
    st.session_state.current_question += 1
    st.session_state.selected_option = None
    st.session_state.answered = False
    st.session_state.start_time = time.time()  # Reset question clock
    if st.session_state.current_question >= len(st.session_state.active_questions):
        st.session_state.quiz_complete = True


# 4. Core Application Routing Layout
st.title("🏆 Ultimate Trivia Challenge")
st.write(
    f"Test your knowledge! Get a random selection of {QUESTIONS_PER_GAME} questions every play session."
)
st.divider()

# Game Over Screen Logic
if st.session_state.quiz_complete:
    st.balloons()
    st.success("🎉 You have finished the quiz!")

    final_score = st.session_state.score
    total_q = len(st.session_state.active_questions)

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

# Active Question Execution Screen
else:
    current_idx = st.session_state.current_question
    q_data = st.session_state.active_questions[current_idx]

    # Calculate time remaining safely upfront
    elapsed_time = time.time() - st.session_state.start_time
    time_left = max(0, int(SECONDS_PER_QUESTION - elapsed_time))

    # Check for timeout before drawing anything new
    if time_left == 0 and not st.session_state.answered:
        st.session_state.answered = True
        st.session_state.selected_option = "TIMEOUT"

    # Live Question Headers
    col1, col2 = st.columns(2)
    with col1:
        st.write(
            f"**Question {current_idx + 1} of {len(st.session_state.active_questions)}**"
        )
    with col2:
        if not st.session_state.answered:
            st.metric(label="⏱️ Time Remaining", value=f"{time_left}s")
        else:
            st.write("")

    st.progress((current_idx) / len(st.session_state.active_questions))

    st.markdown(
        f'<div class="question-box"><h3>{q_data["question"]}</h3></div>',
        unsafe_allow_html=True,
    )

    # Process Form Interaction Context
    if not st.session_state.answered:
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
                    st.rerun()

    # Show Answer Evaluation after submission or timeout action
    if st.session_state.answered:
        user_choice = st.session_state.selected_option
        correct_choice = q_data["answer"]

        if user_choice == "TIMEOUT":
            st.error(
                f"⏰ **Time's up!** You didn't submit an answer in time. The correct answer was: **{correct_choice}**"
            )
        elif user_choice == correct_choice:
            st.success(f"🎯 **Correct!** Excellent choice.")
            if f"scored_{current_idx}" not in st.session_state:
                st.session_state.score += 1
                st.session_state[f"scored_{current_idx}"] = True
        else:
            st.error(f"❌ **Incorrect.** The correct answer was: **{correct_choice}**")

        st.button("Next Question ➡️", on_click=next_question, type="primary")

    # Score tracker sidebar footprint
    with st.sidebar:
        st.header("🏆 Live Stats")
        st.metric(label="Current Score", value=st.session_state.score)
        if st.button("Reset Game"):
            reset_quiz()
            st.rerun()

    # --- CRITICAL TIMER TRICK ---
    # We sleep and rerun at the very *END* of the file code loop.
    # This guarantees Streamlit finishes rendering the entire visual interface before refreshing!
    if time_left > 0 and not st.session_state.answered:
        time.sleep(1)
        st.rerun()



import random
import time
import streamlit as st

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="Ultimate Trivia Championship",
    page_icon="🏆",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom Enhanced CSS for a Modern, Beautiful UI
st.markdown(
    """
    <style>
    .main { padding-top: 1rem; }
    
    /* Beautiful Question Card styling */
    .question-card {
        background: linear-gradient(135px, rgba(255, 75, 75, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
        padding: 30px;
        border-radius: 16px;
        border: 1px solid rgba(255, 75, 75, 0.2);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        margin-bottom: 25px;
    }
    
    /* Modern big headers */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        background: linear-gradient(45deg, #FF4B4B, #FF8585);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    /* Button enhancement */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.2em;
        font-size: 16px;
        font-weight: 700;
        letter-spacing: 0.5px;
        transition: all 0.2s ease-in-out;
    }
    
    /* Radio Option block styling adjustments */
    div[data-testid="stRadio"] label {
        padding: 10px 15px;
        border-radius: 8px;
        background-color: rgba(255, 255, 255, 0.03);
        margin-bottom: 6px;
        transition: background-color 0.2s;
    }
    div[data-testid="stRadio"] label:hover {
        background-color: rgba(255, 75, 75, 0.1);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 2. Master Question Pool
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
        "options": ["Single-responsibility", "Scope-isolation", "Structural-pattern", "State-management"],
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

# Configurable constants
QUESTIONS_PER_GAME = 5
TOTAL_QUIZ_TIME = 60  # 60 seconds for the WHOLE exercise


# 3. Game Management State Engine
def initialize_game():
    selected_questions = random.sample(MASTER_QUIZ_POOL, QUESTIONS_PER_GAME)
    for q in selected_questions:
        q["options"] = list(q["options"])
        random.shuffle(q["options"])

    st.session_state.active_questions = selected_questions
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_complete = False
    st.session_state.selected_option = None
    st.session_state.answered = False
    st.session_state.quiz_start_time = time.time()  # Starts once per game session
    st.session_state.timeout_triggered = False


if "active_questions" not in st.session_state:
    initialize_game()


def reset_quiz():
    initialize_game()


def next_question():
    st.session_state.current_question += 1
    st.session_state.selected_option = None
    st.session_state.answered = False
    if st.session_state.current_question >= len(st.session_state.active_questions):
        st.session_state.quiz_complete = True


# 4. Timer Math Engine (Calculated upfront on script execution)
elapsed_time = time.time() - st.session_state.quiz_start_time
time_left = max(0, int(TOTAL_QUIZ_TIME - elapsed_time))

# Check globally if time ran completely out
if time_left == 0 and not st.session_state.quiz_complete:
    st.session_state.quiz_complete = True
    st.session_state.timeout_triggered = True


# 5. Core Screen Routing
st.markdown('<div class="main-title">🏆 Ultimate Trivia Championship</div>', unsafe_allow_html=True)
st.write("A clean, quick-fire test of technical logic. Can you survive the clock?")
st.divider()

# --- Game Over Screen ---
if st.session_state.quiz_complete:
    if st.session_state.timeout_triggered:
        st.error("⏰ **TIME'S UP!** The clock hit zero before you could finish the championship exercise!")
    else:
        st.balloons()
        st.success("🎉 **Congratulations!** You have completed the exercise.")

    final_score = st.session_state.score
    total_q = len(st.session_state.active_questions)

    # Clean layout summary metrics
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        st.metric(label="Final Score Accuracy", value=f"{final_score} / {total_q}")
    with m_col2:
        time_spent = min(TOTAL_QUIZ_TIME, int(elapsed_time))
        st.metric(label="Total Duration Spent", value=f"{time_spent}s")

    # Feedback Logic
    if final_score == total_q and not st.session_state.timeout_triggered:
        st.subheader("🥇 Flawless Victory! You are a master programmer!")
    elif final_score >= total_q // 2:
        st.subheader("🥈 Great Job! Highly strategic execution.")
    else:
        st.subheader("🥉 Keep Studying! Failure is just a feature waiting to be refactored.")

    if st.button("🔄 Launch New Randomized Session", type="primary"):
        reset_quiz()
        st.rerun()

# --- Active Question Screen ---
else:
    current_idx = st.session_state.current_question
    q_data = st.session_state.active_questions[current_idx]

    # Upper Status Interface Columns
    status_col1, status_col2 = st.columns([2, 1])
    with status_col1:
        st.markdown(f"#### 📝 Question **{current_idx + 1}** of **{len(st.session_state.active_questions)}**")
    with status_col2:
        # Styled color alerts matching timer gravity
        if time_left > 20:
            st.success(f"⏱️ **{time_left}s remaining**")
        elif time_left > 7:
            st.warning(f"⏳ **{time_left}s remaining**")
        else:
            st.error(f"🚨 **{time_left}s remaining!**")

    # Visual Global Timeline Progress Bar (Time Remaining / Total Time)
    time_ratio = time_left / TOTAL_QUIZ_TIME
    st.progress(time_ratio)

    # Beautiful Question Card Layout
    st.markdown(
        f"""
        <div class="question-card">
            <span style="font-size: 14px; text-transform: uppercase; letter-spacing: 1px; color: #FF4B4B; font-weight: bold;">Current Challenge</span>
            <h3 style="margin-top: 5px; margin-bottom: 0;">{q_data["question"]}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Option Form Processing
    if not st.session_state.answered:
        with st.form(key=f"quiz_form_{current_idx}"):
            choice = st.radio(
                "Options Configuration:",
                options=q_data["options"],
                index=None,
                key=f"radio_{current_idx}",
                label_visibility="collapsed",
            )

            submit_btn = st.form_submit_button(
                label="Lock In Selection 🔒", use_container_width=True
            )

            if submit_btn:
                if choice is None:
                    st.warning("Please choose an answer path configuration before submitting!")
                else:
                    st.session_state.selected_option = choice
                    st.session_state.answered = True
                    st.rerun()

    # Evaluation Feedback Box
    if st.session_state.answered:
        user_choice = st.session_state.selected_option
        correct_choice = q_data["answer"]

        if user_choice == correct_choice:
            st.success("🎯 **Correct Entry!** Exceptional logic tracing.")
            if f"scored_{current_idx}" not in st.session_state:
                st.session_state.score += 1
                st.session_state[f"scored_{current_idx}"] = True
        else:
            st.error(f"❌ **Incorrect Pipeline.** The optimized configuration was: **{correct_choice}**")

        st.button("Advance to Next Challenge ➡️", on_click=next_question, type="primary")

    # Enhanced Live Analytics Dashboard inside Sidebar
    with st.sidebar:
        st.markdown("### 🏆 Championship Radar")
        st.metric(label="Current Points Banked", value=f"{st.session_state.score} pts")
        
        # Sub-stats breakdown
        st.markdown("---")
        st.write(f"• **Exercise Speed Target:** {TOTAL_QUIZ_TIME}s limit")




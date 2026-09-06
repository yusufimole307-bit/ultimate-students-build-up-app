import random
import time
import streamlit as st

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="Advanced Science Olympiad",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom Enhanced CSS for a Modern, Smooth UI
st.markdown(
    """
    <style>
    .main { padding-top: 1rem; }
    .question-card {
        background: linear-gradient(135deg, rgba(75, 150, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
        padding: 35px;
        border-radius: 16px;
        border: 1px solid rgba(75, 150, 255, 0.2);
        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.3);
        margin-bottom: 25px;
    }
    .main-title {
        font-size: 38px;
        font-weight: 800;
        background: linear-gradient(45deg, #4B96FF, #00FFCC);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    .subject-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        background-color: rgba(75, 150, 255, 0.15);
        color: #00FFCC;
        border: 1px solid rgba(0,255,204,0.3);
        margin-bottom: 12px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.2em;
        font-size: 16px;
        font-weight: 700;
        transition: all 0.2s ease-in-out;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 2. Deeper Scientific Subject Pool
MASTER_QUIZ_POOL = [
    {
        "subject": "Astrophysics",
        "question": "What mechanism prevents a white dwarf star from collapsing under its own gravitational weight?",
        "options": [
            "Electron degeneracy pressure",
            "Neutron degeneracy pressure",
            "Nuclear fusion radiation pressure",
            "Thermal gas expansion"
        ],
        "answer": "Electron degeneracy pressure",
    },
    {
        "subject": "Quantum Mechanics",
        "question": "Which quantum mechanical principle asserts that two identical fermions cannot occupy the same quantum state simultaneously?",
        "options": [
            "Pauli Exclusion Principle",
            "Heisenberg Uncertainty Principle",
            "Schrödinger Wave Postulate",
            "De Broglie Duality Relation"
        ],
        "answer": "Pauli Exclusion Principle",
    },
    {
        "subject": "Genetics & Molecular Biology",
        "question": "During DNA replication, which specific enzyme is responsible for unwinding the double helix at the replication fork?",
        "options": ["DNA Helicase", "DNA Polymerase III", "Topoisomerase", "RNA Primase"],
        "answer": "DNA Helicase",
    },
    {
        "subject": "Organic Chemistry",
        "question": "Which of the following organic structures describes a hydrocarbon ring architecture featuring alternating single and double bonds with aromatic stability?",
        "options": ["Benzene", "Cyclohexane", "Hexane", "Toluene"],
        "answer": "Benzene",
    },
    {
        "subject": "Thermodynamics",
        "question": "Which law of thermodynamics explicitly defines the concept of Entropy and asserts that isolated systems evolve toward maximum disorder?",
        "options": ["Second Law", "First Law", "Third Law", "Zeroth Law"],
        "answer": "Second Law",
    },
    {
        "subject": "Particle Physics",
        "question": "Which fundamental gauge boson is theoretically responsible for imparting mass to elementary particles via field interactions?",
        "options": ["Higgs Boson", "Gluon", "Photon", "Z Boson"],
        "answer": "Higgs Boson",
    },
    {
        "subject": "Cellular Biochemistry",
        "question": "What molecule acts as the primary terminal electron acceptor at the end of the mitochondrial Electron Transport Chain?",
        "options": ["Oxygen (O2)", "NADH", "Carbon Dioxide (CO2)", "Water (H2O)"],
        "answer": "Oxygen (O2)",
    }
]

QUESTIONS_PER_GAME = 5
TOTAL_GAME_LIMIT = 45  # 45 Seconds allocated for the entire exam challenge


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
    st.session_state.quiz_start_time = time.time()


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


# 4. Silent Background Time Calculation
elapsed_time = time.time() - st.session_state.quiz_start_time
time_left = max(0, int(TOTAL_GAME_LIMIT - elapsed_time))

# Evaluate global timeline parameters
if time_left <= 0 and not st.session_state.quiz_complete:
    st.session_state.quiz_complete = True


# 5. Core Screen Routing
st.markdown('<div class="main-title">🧬 Advanced Science Olympiad</div>', unsafe_allow_html=True)
st.write("A lag-free, precision examination environment tracking strategic speed and scientific depth.")
st.divider()

# --- Game Over Screen ---
if st.session_state.quiz_complete:
    if time_left <= 0:
        st.error("⏰ **TIME EXPIRED!** The master exam window closed before complete submission could be recorded.")
    else:
        st.balloons()
        st.success("🎉 **Examination Process Complete.** Data logged successfully.")

    final_score = st.session_state.score
    total_q = len(st.session_state.active_questions)

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Validated Accuracy", value=f"{final_score} / {total_q}")
    with col2:
        st.metric(label="Total Time Elapsed", value=f"{int(elapsed_time)}s / {TOTAL_GAME_LIMIT}s")

    if final_score == total_q and time_left > 0:
        st.subheader("🥇 Exceptional Performance! Elite tier scientific proficiency.")
    elif final_score >= total_q // 2:
        st.subheader("🥈 Academic Pass. Research parameters verified.")
    else:
        st.subheader("🥉 Low Yield. Re-verify source variables and try again.")

    if st.button("🔄 Initialize New Examination Instance", type="primary"):
        reset_quiz()
        st.rerun()

# --- Active Question Screen (100% Smooth UI) ---
else:
    current_idx = st.session_state.current_question
    q_data = st.session_state.active_questions[current_idx]

    # Metrics Display (Updates statically on interaction)
    status_col1, status_col2 = st.columns(2)
    with status_col1:
        st.markdown(f"#### 🧪 Core Matrix **{current_idx + 1}** of **{len(st.session_state.active_questions)}**")
    with status_col2:
        st.markdown(f"<div style='text-align: right; color: #4B96FF; font-weight: bold;'>⏳ Estimated Game Time Remaining: ~{time_left}s</div>", unsafe_allow_html=True)

    # Question Card Wrapper
    st.markdown(
        f"""
        <div class="question-card">
            <div class="subject-badge">{q_data["subject"]}</div>
            <h3 style="margin: 0; font-weight: 600; line-height: 1.4;">{q_data["question"]}</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Process Form Interaction Context
    if not st.session_state.answered:
        with st.form(key=f"science_form_{current_idx}"):
            choice = st.radio(
                "Select configuration mapping:",
                options=q_data["options"],
                index=None,
                key=f"radio_{current_idx}",
                label_visibility="collapsed",
            )

            submit_btn = st.form_submit_button(
                label="Commit Selection to Registry 🔒", use_container_width=True
            )

            if submit_btn:
                if choice is None:
                    st.warning("You must declare a variable selection pathway before locking in configuration.")
                else:
                    # Final safety check: Check time at the exact moment button is pressed
                    current_check_time = time.time() - st.session_state.quiz_start_time
                    if current_check_time >= TOTAL_GAME_LIMIT:
                        st.session_state.quiz_complete = True
                        st.rerun()
                    else:
                        st.session_state.selected_option = choice
                        st.session_state.answered = True
                        st.rerun()

    # Evaluation Feedback Box
    if st.session_state.answered:
        user_choice = st.session_state.selected_option
        correct_choice = q_data["answer"]

        if user_choice == correct_choice:
            st.success("🎯 **Correct Evaluation.** Entry maps cleanly to source truth records.")
            if f"scored_{current_idx}" not in st.session_state:
                st.session_state.score += 1
                st.session_state[f"scored_{current_idx}"] = True
        else:
            st.error(f"❌ **Anomalous Analysis.** The correct verified state is: **{correct_choice}**")

        st.button("Advance to Next System Node ➡️", on_click=next_question, type="primary")

    # Side Management Matrix Footprint
    with st.sidebar:
        st.markdown("### 🏆 Live Analysis")
        st.metric(label="Current Points Banked", value=f"{st.session_state.score} / {QUESTIONS_PER_GAME}")
        st.progress((current_idx) / QUESTIONS_PER_GAME)
        st.markdown("---")
        st.write("• **Timing Engine:** On-Action Calculation")





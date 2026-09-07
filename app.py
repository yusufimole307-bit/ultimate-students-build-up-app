import random
import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Ultimate Trivia Challenge",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
        /* ---------- Global ---------- */
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(75,150,255,0.08), transparent 30%),
                radial-gradient(circle at top right, rgba(255,75,75,0.07), transparent 25%),
                #0b1020;
        }

        .main {
            padding-top: 1rem;
        }

        /* ---------- Header ---------- */
        .hero {
            text-align: center;
            padding: 15px 10px 25px 10px;
        }

        .hero-title {
            font-size: clamp(32px, 5vw, 58px);
            font-weight: 900;
            margin-bottom: 5px;
            background: linear-gradient(
                90deg,
                #ff4b4b,
                #ff8a65,
                #4b96ff,
                #7c4dff
            );
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-subtitle {
            color: #9ca3af;
            font-size: 17px;
            margin-top: 0;
        }

        /* ---------- Cards ---------- */
        .card {
            background: rgba(255,255,255,0.055);
            border: 1px solid rgba(255,255,255,0.10);
            border-radius: 18px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 10px 35px rgba(0,0,0,0.20);
            backdrop-filter: blur(10px);
        }

        .question-card {
            background: linear-gradient(
                145deg,
                rgba(255,255,255,0.075),
                rgba(255,255,255,0.025)
            );
            border: 1px solid rgba(75,150,255,0.20);
            border-radius: 22px;
            padding: 30px;
            margin: 15px 0 20px 0;
            box-shadow: 0 15px 45px rgba(0,0,0,0.25);
        }

        .question-number {
            color: #60a5fa;
            font-weight: 800;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .question-text {
            color: #f9fafb;
            font-size: clamp(21px, 3vw, 30px);
            line-height: 1.35;
            font-weight: 750;
            margin-top: 12px;
        }

        /* ---------- Badges ---------- */
        .badge {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-right: 6px;
        }

        .category {
            background: rgba(75,150,255,0.14);
            color: #60a5fa;
            border: 1px solid rgba(75,150,255,0.25);
        }

        .easy {
            background: rgba(34,197,94,0.13);
            color: #4ade80;
            border: 1px solid rgba(34,197,94,0.25);
        }

        .medium {
            background: rgba(245,158,11,0.13);
            color: #fbbf24;
            border: 1px solid rgba(245,158,11,0.25);
        }

        .hard {
            background: rgba(239,68,68,0.13);
            color: #f87171;
            border: 1px solid rgba(239,68,68,0.25);
        }

        /* ---------- Stats ---------- */
        .stat-card {
            background: rgba(255,255,255,0.045);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 18px;
            text-align: center;
            min-height: 105px;
        }

        .stat-value {
            font-size: 27px;
            font-weight: 850;
            color: #ffffff;
        }

        .stat-label {
            font-size: 12px;
            color: #9ca3af;
            margin-top: 3px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }

        /* ---------- Result ---------- */
        .result-card {
            text-align: center;
            background: linear-gradient(
                145deg,
                rgba(75,150,255,0.12),
                rgba(124,77,255,0.08)
            );
            border: 1px solid rgba(96,165,250,0.25);
            border-radius: 24px;
            padding: 45px 25px;
            margin-top: 25px;
        }

        .result-score {
            font-size: 70px;
            font-weight: 900;
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .result-title {
            font-size: 30px;
            font-weight: 800;
            color: white;
        }

        .result-message {
            color: #9ca3af;
            font-size: 16px;
        }

        /* ---------- Sidebar ---------- */
        section[data-testid="stSidebar"] {
            background: #080d1a;
            border-right: 1px solid rgba(255,255,255,0.08);
        }

        .sidebar-title {
            font-size: 20px;
            font-weight: 850;
            color: white;
            margin-bottom: 5px;
        }

        .sidebar-caption {
            color: #6b7280;
            font-size: 13px;
            margin-bottom: 20px;
        }

        /* ---------- Buttons ---------- */
        .stButton > button {
            width: 100%;
            border-radius: 12px;
            min-height: 46px;
            font-weight: 750;
            border: 1px solid rgba(255,255,255,0.10);
            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-1px);
            border-color: rgba(96,165,250,0.45);
            box-shadow: 0 6px 20px rgba(0,0,0,0.20);
        }

        /* ---------- Radio ---------- */
        div[role="radiogroup"] {
            gap: 10px;
        }

        /* ---------- Footer ---------- */
        .footer {
            text-align: center;
            color: #6b7280;
            font-size: 12px;
            padding: 35px 0 10px 0;
        }

        /* ---------- Mobile ---------- */
        @media (max-width: 768px) {
            .question-card {
                padding: 20px;
            }

            .card {
                padding: 18px;
            }

            .result-score {
                font-size: 52px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# TRIVIA DATA
# ============================================================

QUESTIONS = [
    # ---------------- GENERAL KNOWLEDGE ----------------
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Saturn", "Jupiter", "Neptune"],
        "answer": "Jupiter",
        "category": "General Knowledge",
        "difficulty": "Easy",
    },
    {
        "question": "Which element has the chemical symbol Au?",
        "options": ["Silver", "Gold", "Argon", "Copper"],
        "answer": "Gold",
        "category": "General Knowledge",
        "difficulty": "Easy",
    },
    {
        "question": "Who wrote the novel '1984'?",
        "options": ["George Orwell", "Aldous Huxley", "Ernest Hemingway", "J.R.R. Tolkien"],
        "answer": "George Orwell",
        "category": "General Knowledge",
        "difficulty": "Medium",
    },
    {
        "question": "Which instrument has 88 keys on a standard version?",
        "options": ["Violin", "Piano", "Guitar", "Flute"],
        "answer": "Piano",
        "category": "General Knowledge",
        "difficulty": "Easy",
    },
    {
        "question": "What is the hardest naturally occurring mineral?",
        "options": ["Quartz", "Diamond", "Titanium", "Graphite"],
        "answer": "Diamond",
        "category": "General Knowledge",
        "difficulty": "Easy",
    },

    # ---------------- TECH / CS ----------------
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Core Processing Utility",
        ],
        "answer": "Central Processing Unit",
        "category": "Tech/CS",
        "difficulty": "Easy",
    },
    {
        "question": "Which language is primarily used to style web pages?",
        "options": ["HTML", "Python", "CSS", "SQL"],
        "answer": "CSS",
        "category": "Tech/CS",
        "difficulty": "Easy",
    },
    {
        "question": "Which data structure follows LIFO?",
        "options": ["Queue", "Stack", "Array", "Graph"],
        "answer": "Stack",
        "category": "Tech/CS",
        "difficulty": "Medium",
    },
    {
        "question": "What does API stand for?",
        "options": [
            "Application Programming Interface",
            "Advanced Program Integration",
            "Application Process Instruction",
            "Automated Programming Input",
        ],
        "answer": "Application Programming Interface",
        "category": "Tech/CS",
        "difficulty": "Medium",
    },
    {
        "question": "Which sorting algorithm has an average time complexity of O(n log n)?",
        "options": ["Bubble Sort", "Merge Sort", "Linear Search", "Selection Sort"],
        "answer": "Merge Sort",
        "category": "Tech/CS",
        "difficulty": "Medium",
    },

    # ---------------- SCIENCE / MATH ----------------
    {
        "question": "What is the approximate value of pi?",
        "options": ["2.14", "3.14", "4.14", "5.14"],
        "answer": "3.14",
        "category": "Science/Math",
        "difficulty": "Easy",
    },
    {
        "question": "What gas do plants primarily absorb during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "answer": "Carbon dioxide",
        "category": "Science/Math",
        "difficulty": "Easy",
    },
    {
        "question": "What is the SI unit of force?",
        "options": ["Joule", "Pascal", "Newton", "Watt"],
        "answer": "Newton",
        "category": "Science/Math",
        "difficulty": "Medium",
    },
    {
        "question": "What is the square root of 144?",
        "options": ["10", "11", "12", "14"],
        "answer": "12",
        "category": "Science/Math",
        "difficulty": "Easy",
    },
    {
        "question": "Which particle has a negative electric charge?",
        "options": ["Proton", "Neutron", "Electron", "Photon"],
        "answer": "Electron",
        "category": "Science/Math",
        "difficulty": "Easy",
    },

    # ---------------- HISTORY ----------------
    {
        "question": "In which year did World War II end?",
        "options": ["1942", "1945", "1948", "1950"],
        "answer": "1945",
        "category": "History",
        "difficulty": "Easy",
    },
    {
        "question": "Who was the first president of the United States?",
        "options": [
            "Abraham Lincoln",
            "George Washington",
            "Thomas Jefferson",
            "John Adams",
        ],
        "answer": "George Washington",
        "category": "History",
        "difficulty": "Easy",
    },
    {
        "question": "Which ancient civilization built Machu Picchu?",
        "options": ["Roman", "Egyptian", "Inca", "Mayan"],
        "answer": "Inca",
        "category": "History",
        "difficulty": "Medium",
    },
    {
        "question": "The Renaissance began primarily in which country?",
        "options": ["France", "Italy", "Germany", "Spain"],
        "answer": "Italy",
        "category": "History",
        "difficulty": "Medium",
    },
    {
        "question": "Who was known as the Maid of Orléans?",
        "options": ["Cleopatra", "Joan of Arc", "Marie Curie", "Catherine de Medici"],
        "answer": "Joan of Arc",
        "category": "History",
        "difficulty": "Easy",
    },

    # ---------------- GEOGRAPHY ----------------
    {
        "question": "What is the capital city of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "answer": "Canberra",
        "category": "Geography",
        "difficulty": "Medium",
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific",
        "category": "Geography",
        "difficulty": "Easy",
    },
    {
        "question": "Which country has the largest land area in the world?",
        "options": ["Canada", "China", "United States", "Russia"],
        "answer": "Russia",
        "category": "Geography",
        "difficulty": "Easy",
    },
    {
        "question": "Mount Everest is part of which mountain range?",
        "options": ["Andes", "Alps", "Himalayas", "Rockies"],
        "answer": "Himalayas",
        "category": "Geography",
        "difficulty": "Easy",
    },
    {
        "question": "Which desert is the largest hot desert in the world?",
        "options": ["Gobi", "Sahara", "Kalahari", "Atacama"],
        "answer": "Sahara",
        "category": "Geography",
        "difficulty": "Easy",
    },

    # ---------------- NIGERIA ----------------
    {
        "question": "What is the capital of Nigeria?",
        "options": ["Lagos", "Abuja", "Ibadan", "Kano"],
        "answer": "Abuja",
        "category": "Nigeria",
        "difficulty": "Easy",
    },
    {
        "question": "How many states are there in Nigeria?",
        "options": ["30", "34", "36", "40"],
        "answer": "36",
        "category": "Nigeria",
        "difficulty": "Easy",
    },
    {
        "question": "Which city is widely regarded as Nigeria's commercial capital?",
        "options": ["Abuja", "Lagos", "Kaduna", "Enugu"],
        "answer": "Lagos",
        "category": "Nigeria",
        "difficulty": "Easy",
    },
    {
        "question": "What is the currency of Nigeria?",
        "options": ["Cedi", "Naira", "Shilling", "Franc"],
        "answer": "Naira",
        "category": "Nigeria",
        "difficulty": "Easy",
    },
    {
        "question": "Which river is one of the major rivers of Nigeria?",
        "options": ["Niger River", "Nile River", "Congo River", "Zambezi River"],
        "answer": "Niger River",
        "category": "Nigeria",
        "difficulty": "Easy",
    },
    {
        "question": "Nigeria gained independence from Britain in which year?",
        "options": ["1957", "1960", "1963", "1970"],
        "answer": "1960",
        "category": "Nigeria",
        "difficulty": "Easy",
    },
]


# ============================================================
# SESSION STATE
# ============================================================

def setup_state():
    defaults = {
        "quiz_questions": [],
        "current_question": 0,
        "score": 0,
        "answered": False,
        "selected_answer": None,
        "quiz_finished": False,
        "quiz_started": False,
        "correct_answers": 0,
        "wrong_answers": 0,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


setup_state()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_filtered_questions(category, difficulty):
    pool = [
        q
        for q in QUESTIONS
        if (category == "All Categories" or q["category"] == category)
        and (difficulty == "All Difficulties" or q["difficulty"] == difficulty)
    ]

    random.shuffle(pool)

    return pool[: min(10, len(pool))]


def start_new_quiz(category, difficulty):
    pool = get_filtered_questions(category, difficulty)

    if not pool:
        st.error("No questions match your selected filters.")
        return

    st.session_state.quiz_questions = pool
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.correct_answers = 0
    st.session_state.wrong_answers = 0
    st.session_state.answered = False
    st.session_state.selected_answer = None
    st.session_state.quiz_finished = False
    st.session_state.quiz_started = True


def submit_answer():
    if st.session_state.selected_answer is None:
        st.warning("Please select an answer first.")
        return

    if st.session_state.answered:
        return

    question = st.session_state.quiz_questions[
        st.session_state.current_question
    ]

    st.session_state.answered = True

    if st.session_state.selected_answer == question["answer"]:
        st.session_state.score += 1
        st.session_state.correct_answers += 1
    else:
        st.session_state.wrong_answers += 1


def next_question():
    st.session_state.current_question += 1
    st.session_state.selected_answer = None
    st.session_state.answered = False

    if (
        st.session_state.current_question
        >= len(st.session_state.quiz_questions)
    ):
        st.session_state.quiz_finished = True


def restart_quiz():
    st.session_state.quiz_questions = []
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.correct_answers = 0
    st.session_state.wrong_answers = 0
    st.session_state.answered = False
    st.session_state.selected_answer = None
    st.session_state.quiz_finished = False
    st.session_state.quiz_started = False


def get_result_message(score, total):
    percentage = (score / total) * 100 if total else 0

    if percentage == 100:
        return "🏆 Perfect Score!", "Absolutely outstanding. You got every question right!"
    elif percentage >= 80:
        return "🔥 Excellent Performance!", "You clearly know your stuff. Fantastic result!"
    elif percentage >= 60:
        return "👏 Great Job!", "Solid performance. A little more practice and you'll be elite."
    elif percentage >= 40:
        return "💪 Keep Going!", "You're making progress. Keep learning and try again."
    else:
        return "📚 Keep Practicing!", "Every great trivia champion starts somewhere."


# ============================================================
# SIDEBAR
# ============================================================

categories = sorted(set(q["category"] for q in QUESTIONS))
difficulties = ["Easy", "Medium", "Hard"]

with st.sidebar:
    st.markdown(
        '<div class="sidebar-title">🏆 TRIVIA HQ</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-caption">Configure your challenge</div>',
        unsafe_allow_html=True,
    )

    selected_category = st.selectbox(
        "Category",
        ["All Categories"] + categories,
        key="category_filter",
    )

    selected_difficulty = st.selectbox(
        "Difficulty",
        ["All Difficulties"] + difficulties,
        key="difficulty_filter",
    )

    st.divider()

    available = get_filtered_questions(
        selected_category,
        selected_difficulty,
    )

    st.markdown("### 📊 Challenge Info")

    st.metric(
        "Available Questions",
        len(available),
    )

    st.metric(
        "Questions / Game",
        min(10, len(available)),
    )

    st.divider()

    if st.button(
        "🚀 Start New Challenge",
        use_container_width=True,
        type="primary",
    ):
        start_new_quiz(
            selected_category,
            selected_difficulty,
        )
        st.rerun()

    if st.session_state.quiz_started:
        if st.button(
            "🔄 Reset Game",
            use_container_width=True,
        ):
            restart_quiz()
            st.rerun()

    st.markdown(
        """
        <div class="footer">
            Ultimate Trivia Challenge<br>
            Built with Streamlit
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">🏆 ULTIMATE TRIVIA</div>
        <div class="hero-subtitle">
            Test your knowledge. Beat your score. Become the champion.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# LANDING SCREEN
# ============================================================

if not st.session_state.quiz_started:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-value">🌍</div>
                <div class="stat-label">Multiple Categories</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-value">⚡</div>
                <div class="stat-label">3 Difficulty Levels</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-value">🎯</div>
                <div class="stat-label">Instant Feedback</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="card">
            <h2>Ready for the challenge?</h2>
            <p style="color:#9ca3af;">
                Choose a category and difficulty from the sidebar,
                then start your trivia challenge.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "💡 Tip: Your quiz contains up to 10 randomly selected questions "
        "from your chosen filters."
    )

    st.stop()


# ============================================================
# RESULTS SCREEN
# ============================================================

if st.session_state.quiz_finished:

    score = st.session_state.score
    total = len(st.session_state.quiz_questions)

    title, message = get_result_message(score, total)

    percentage = round((score / total) * 100) if total else 0

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-score">{score}/{total}</div>
            <div class="result-title">{title}</div>
            <div class="result-message">{message}</div>
            <br>
            <div class="result-message">
                Final Score: <strong>{percentage}%</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-value">✅ {st.session_state.correct_answers}</div>
                <div class="stat-label">Correct</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-value">❌ {st.session_state.wrong_answers}</div>
                <div class="stat-label">Incorrect</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-value">🎯 {percentage}%</div>
                <div class="stat-label">Accuracy</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    if st.button(
        "🚀 Play Again",
        type="primary",
        use_container_width=True,
    ):
        start_new_quiz(
            selected_category,
            selected_difficulty,
        )
        st.rerun()

    st.stop()


# ============================================================
# ACTIVE QUIZ
# ============================================================

question_index = st.session_state.current_question
question = st.session_state.quiz_questions[question_index]

total_questions = len(st.session_state.quiz_questions)
display_number = question_index + 1
progress = display_number / total_questions


# ---------- Top Stats ----------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-value">{display_number}/{total_questions}</div>
            <div class="stat-label">Question</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-value">🏆 {st.session_state.score}</div>
            <div class="stat-label">Score</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-value">✅ {st.session_state.correct_answers}</div>
            <div class="stat-label">Correct</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-value">{round(progress * 100)}%</div>
            <div class="stat-label">Progress</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.progress(progress)


# ============================================================
# QUESTION CARD
# ============================================================

difficulty_class = question["difficulty"].lower()

st.markdown(
    f"""
    <div class="question-card">
        <span class="badge category">{question["category"]}</span>
        <span class="badge {difficulty_class}">
            {question["difficulty"]}
        </span>

        <div class="question-number">
            Question {display_number}
        </div>

        <div class="question-text">
            {question["question"]}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# ANSWERS
# ============================================================

st.markdown("### Choose your answer")

st.radio(
    "Answer options",
    question["options"],
    index=None,
    key="selected_answer",
    label_visibility="collapsed",
    disabled=st.session_state.answered,
)


# ============================================================
# SUBMIT / FEEDBACK
# ============================================================

if not st.session_state.answered:

    if st.button(
        "✓ Submit Answer",
        type="primary",
        use_container_width=True,
    ):
        submit_answer()
        st.rerun()

else:

    if st.session_state.selected_answer == question["answer"]:

        st.success(
            f"🎉 Correct! **{question['answer']}** is the right answer."
        )

    else:

        st.error(
            f"❌ Incorrect. The correct answer is "
            f"**{question['answer']}**."
        )

    st.write("")

    if display_number < total_questions:

        if st.button(
            "➡️ Next Question",
            type="primary",
            use_container_width=True,
        ):
            next_question()
            st.rerun()

    else:

        if st.button(
            "🏆 View Final Results",
            type="primary",
            use_container_width=True,
        ):
            next_question()
            st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🏆 Ultimate Trivia Challenge &nbsp;•&nbsp;
        Streamlit Edition
    </div>
    """,
    unsafe_allow_html=True,
)

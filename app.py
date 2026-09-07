import random
import streamlit as st

# ============================================================
# PAGE CONFIG
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

    /* =========================
       GLOBAL
    ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 0%,
                rgba(75, 150, 255, 0.12),
                transparent 28%
            ),
            radial-gradient(
                circle at 90% 0%,
                rgba(255, 75, 75, 0.10),
                transparent 28%
            ),
            #080d19;
    }

    .main {
        padding-top: 1rem;
    }

    /* =========================
       HERO
    ========================= */

    .hero {
        text-align: center;
        padding: 10px 10px 28px 10px;
    }

    .hero-title {
        font-size: clamp(34px, 5vw, 58px);
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 8px;

        background: linear-gradient(
            90deg,
            #ff4b4b,
            #ff8a65,
            #4b96ff,
            #8b5cf6
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        color: #9ca3af;
        font-size: 16px;
        margin: 0;
    }

    /* =========================
       CARDS
    ========================= */

    .card {
        background: rgba(255, 255, 255, 0.045);
        border: 1px solid rgba(255, 255, 255, 0.09);
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.20);
    }

    .question-card {
        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.075),
                rgba(255,255,255,0.025)
            );

        border: 1px solid rgba(75, 150, 255, 0.22);
        border-radius: 22px;
        padding: 30px;
        margin: 18px 0 24px 0;

        box-shadow:
            0 15px 45px rgba(0,0,0,0.25);
    }

    .question-number {
        color: #60a5fa;
        font-size: 13px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 14px;
    }

    .question-text {
        color: #f9fafb;
        font-size: clamp(21px, 3vw, 30px);
        font-weight: 750;
        line-height: 1.4;
        margin-top: 8px;
    }

    /* =========================
       BADGES
    ========================= */

    .badge {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 999px;
        font-size: 10px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-right: 6px;
    }

    .category {
        background: rgba(75, 150, 255, 0.13);
        color: #60a5fa;
        border: 1px solid rgba(75, 150, 255, 0.25);
    }

    .easy {
        background: rgba(34, 197, 94, 0.13);
        color: #4ade80;
        border: 1px solid rgba(34, 197, 94, 0.25);
    }

    .medium {
        background: rgba(245, 158, 11, 0.13);
        color: #fbbf24;
        border: 1px solid rgba(245, 158, 11, 0.25);
    }

    .hard {
        background: rgba(239, 68, 68, 0.13);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.25);
    }

    /* =========================
       STAT CARDS
    ========================= */

    .stat-card {
        background: rgba(255, 255, 255, 0.045);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 17px 10px;
        text-align: center;
        min-height: 95px;
    }

    .stat-value {
        color: #ffffff;
        font-size: 26px;
        font-weight: 850;
    }

    .stat-label {
        color: #8b95a7;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-top: 3px;
    }

    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background: #070b15;
        border-right: 1px solid rgba(255,255,255,0.07);
    }

    .sidebar-title {
        color: #ffffff;
        font-size: 21px;
        font-weight: 850;
    }

    .sidebar-caption {
        color: #6b7280;
        font-size: 13px;
        margin-bottom: 20px;
    }

    /* =========================
       BUTTONS
    ========================= */

    .stButton > button {
        width: 100%;
        min-height: 46px;
        border-radius: 12px;
        font-weight: 750;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
    }

    /* =========================
       RESULTS
    ========================= */

    .result-card {
        text-align: center;
        padding: 45px 20px;

        background:
            linear-gradient(
                145deg,
                rgba(75,150,255,0.13),
                rgba(124,77,255,0.08)
            );

        border: 1px solid rgba(96,165,250,0.25);
        border-radius: 24px;

        box-shadow: 0 20px 55px rgba(0,0,0,0.25);
    }

    .result-score {
        font-size: clamp(50px, 8vw, 76px);
        font-weight: 900;

        background: linear-gradient(
            90deg,
            #60a5fa,
            #a78bfa
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .result-title {
        color: #ffffff;
        font-size: 30px;
        font-weight: 850;
        margin-top: 5px;
    }

    .result-message {
        color: #9ca3af;
        font-size: 16px;
    }

    /* =========================
       FOOTER
    ========================= */

    .footer {
        color: #5f6878;
        text-align: center;
        font-size: 12px;
        padding: 35px 0 10px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# QUESTION DATABASE
# ============================================================

QUESTIONS = [

    # ========================================================
    # GENERAL KNOWLEDGE
    # ========================================================

    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Saturn", "Jupiter", "Neptune"],
        "answer": "Jupiter",
        "category": "General Knowledge",
        "difficulty": "Easy",
    },

    {
        "question": "Which element has the chemical symbol Au?",
        "options": ["Silver", "Gold", "Copper", "Argon"],
        "answer": "Gold",
        "category": "General Knowledge",
        "difficulty": "Easy",
    },

    {
        "question": "Who wrote the novel '1984'?",
        "options": [
            "George Orwell",
            "Aldous Huxley",
            "Ernest Hemingway",
            "J.R.R. Tolkien",
        ],
        "answer": "George Orwell",
        "category": "General Knowledge",
        "difficulty": "Medium",
    },

    {
        "question": "Which instrument traditionally has 88 keys?",
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

    {
        "question": "Which language has the most native speakers worldwide?",
        "options": ["English", "Spanish", "Mandarin Chinese", "Hindi"],
        "answer": "Mandarin Chinese",
        "category": "General Knowledge",
        "difficulty": "Medium",
    },

    # ========================================================
    # TECH / CS
    # ========================================================

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
        "question": "Which technology is primarily used to style web pages?",
        "options": ["HTML", "Python", "CSS", "SQL"],
        "answer": "CSS",
        "category": "Tech/CS",
        "difficulty": "Easy",
    },

    {
        "question": "Which data structure follows the LIFO principle?",
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
        "question": "Which algorithm has an average time complexity of O(n log n)?",
        "options": [
            "Bubble Sort",
            "Merge Sort",
            "Linear Search",
            "Selection Sort",
        ],
        "answer": "Merge Sort",
        "category": "Tech/CS",
        "difficulty": "Medium",
    },

    {
        "question": "Which protocol is commonly used to securely browse websites?",
        "options": ["HTTP", "HTTPS", "FTP", "SMTP"],
        "answer": "HTTPS",
        "category": "Tech/CS",
        "difficulty": "Easy",
    },

    # ========================================================
    # SCIENCE / MATH
    # ========================================================

    {
        "question": "What is the approximate value of pi?",
        "options": ["2.14", "3.14", "4.14", "5.14"],
        "answer": "3.14",
        "category": "Science/Math",
        "difficulty": "Easy",
    },

    {
        "question": "Which gas do plants absorb during photosynthesis?",
        "options": [
            "Oxygen",
            "Nitrogen",
            "Carbon dioxide",
            "Hydrogen",
        ],
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
        "question": "Which particle carries a negative electric charge?",
        "options": ["Proton", "Neutron", "Electron", "Photon"],
        "answer": "Electron",
        "category": "Science/Math",
        "difficulty": "Easy",
    },

    {
        "question": "What is the chemical formula for water?",
        "options": ["CO2", "H2O", "O2", "NaCl"],
        "answer": "H2O",
        "category": "Science/Math",
        "difficulty": "Easy",
    },

    # ========================================================
    # HISTORY
    # ========================================================

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
        "question": "Which civilization built Machu Picchu?",
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
        "options": [
            "Cleopatra",
            "Joan of Arc",
            "Marie Curie",
            "Catherine de Medici",
        ],
        "answer": "Joan of Arc",
        "category": "History",
        "difficulty": "Easy",
    },

    # ========================================================
    # GEOGRAPHY
    # ========================================================

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
        "question": "Which country has the largest land area?",
        "options": ["Canada", "China", "United States", "Russia"],
        "answer": "Russia",
        "category": "Geography",
        "difficulty": "Easy",
    },

    {
        "question": "Mount Everest belongs to which mountain range?",
        "options": ["Andes", "Alps", "Himalayas", "Rockies"],
        "answer": "Himalayas",
        "category": "Geography",
        "difficulty": "Easy",
    },

    {
        "question": "Which is the world's largest hot desert?",
        "options": ["Gobi", "Sahara", "Kalahari", "Atacama"],
        "answer": "Sahara",
        "category": "Geography",
        "difficulty": "Easy",
    },

    # ========================================================
    # NIGERIA
    # ========================================================

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
        "question": "Nigeria gained independence from Britain in which year?",
        "options": ["1957", "1960", "1963", "1970"],
        "answer": "1960",
        "category": "Nigeria",
        "difficulty": "Easy",
    },

    {
        "question": "Which city is the capital of Oyo State?",
        "options": ["Ogbomoso", "Ibadan", "Iseyin", "Oyo"],
        "answer": "Ibadan",
        "category": "Nigeria",
        "difficulty": "Easy",
    },
]


# ============================================================
# SESSION STATE
# ============================================================

DEFAULT_STATE = {
    "quiz_started": False,
    "quiz_finished": False,
    "quiz_questions": [],
    "question_index": 0,
    "score": 0,
    "correct_answers": 0,
    "wrong_answers": 0,
    "answered": False,
    "answer": None,
}


for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# FUNCTIONS
# ============================================================

def get_question_pool(category, difficulty):
    """Return questions matching the selected filters."""

    return [
        q
        for q in QUESTIONS
        if (
            category == "All Categories"
            or q["category"] == category
        )
        and (
            difficulty == "All Difficulties"
            or q["difficulty"] == difficulty
        )
    ]


def start_quiz(category, difficulty):
    """Start a fresh quiz."""

    pool = get_question_pool(category, difficulty)

    if not pool:
        st.error(
            "No questions are available for those filters."
        )
        return False

    random.shuffle(pool)

    # Maximum 10 questions per game
    st.session_state.quiz_questions = pool[:10]

    st.session_state.quiz_started = True
    st.session_state.quiz_finished = False
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.correct_answers = 0
    st.session_state.wrong_answers = 0
    st.session_state.answered = False
    st.session_state.answer = None

    return True


def submit_answer(answer):
    """Evaluate an answer exactly once."""

    if st.session_state.answered:
        return

    if answer is None:
        st.warning("Please select an answer.")
        return

    current_question = st.session_state.quiz_questions[
        st.session_state.question_index
    ]

    st.session_state.answer = answer
    st.session_state.answered = True

    if answer == current_question["answer"]:
        st.session_state.score += 1
        st.session_state.correct_answers += 1
    else:
        st.session_state.wrong_answers += 1


def go_to_next_question():
    """Move to the next question."""

    st.session_state.question_index += 1

    st.session_state.answer = None
    st.session_state.answered = False

    if (
        st.session_state.question_index
        >= len(st.session_state.quiz_questions)
    ):
        st.session_state.quiz_finished = True


def reset_game():
    """Completely reset the game."""

    for key, value in DEFAULT_STATE.items():
        st.session_state[key] = value


def result_message(score, total):
    """Return result title and message."""

    if total == 0:
        return "No Score", "Start a new challenge."

    percentage = (score / total) * 100

    if percentage == 100:
        return (
            "🏆 Perfect Score!",
            "Outstanding! You answered every question correctly.",
        )

    if percentage >= 80:
        return (
            "🔥 Excellent!",
            "Fantastic performance. You're clearly a trivia champion.",
        )

    if percentage >= 60:
        return (
            "👏 Great Job!",
            "Strong performance. Keep pushing for an even higher score.",
        )

    if percentage >= 40:
        return (
            "💪 Good Effort!",
            "You're getting there. Keep practicing and try again.",
        )

    return (
        "📚 Keep Learning!",
        "Don't give up. Every attempt makes you better.",
    )


# ============================================================
# SIDEBAR
# ============================================================

categories = sorted(
    {q["category"] for q in QUESTIONS}
)

difficulty_options = [
    "All Difficulties",
    "Easy",
    "Medium",
    "Hard",
]


with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🏆 TRIVIA HQ</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-caption">'
        'Build your perfect challenge'
        '</div>',
        unsafe_allow_html=True,
    )

    selected_category = st.selectbox(
        "Category",
        ["All Categories"] + categories,
    )

    selected_difficulty = st.selectbox(
        "Difficulty",
        difficulty_options,
    )

    st.divider()

    available_questions = get_question_pool(
        selected_category,
        selected_difficulty,
    )

    st.markdown("### 📊 Challenge Info")

    st.metric(
        "Available",
        len(available_questions),
    )

    st.metric(
        "Questions / Game",
        min(10, len(available_questions)),
    )

    st.divider()

    if st.button(
        "🚀 Start Challenge",
        type="primary",
        use_container_width=True,
    ):
        if start_quiz(
            selected_category,
            selected_difficulty,
        ):
            st.rerun()

    if st.session_state.quiz_started:

        if st.button(
            "🔄 Reset Game",
            use_container_width=True,
        ):
            reset_game()
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
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-title">
            🏆 ULTIMATE TRIVIA
        </div>

        <div class="hero-subtitle">
            Test your knowledge • Challenge yourself • Become the champion
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# LANDING PAGE
# ============================================================

if not st.session_state.quiz_started:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-value">🌍</div>
                <div class="stat-label">
                    Multiple Categories
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-value">⚡</div>
                <div class="stat-label">
                    Multiple Difficulties
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-value">🎯</div>
                <div class="stat-label">
                    Instant Feedback
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    st.markdown(
        """
        <div class="card">

            <h2>Ready to test your knowledge?</h2>

            <p style="color:#9ca3af;">
                Select your category and difficulty from the
                sidebar, then launch your challenge.
            </p>

            <p style="color:#9ca3af;">
                Each game contains up to
                <strong>10 randomly selected questions.</strong>
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "💡 Choose a category and difficulty, then click "
        "'Start Challenge' in the sidebar."
    )

    st.stop()


# ============================================================
# RESULTS PAGE
# ============================================================

if st.session_state.quiz_finished:

    score = st.session_state.score
    total = len(st.session_state.quiz_questions)

    percentage = (
        round((score / total) * 100)
        if total
        else 0
    )

    title, message = result_message(
        score,
        total,
    )

    st.markdown(
        f"""
        <div class="result-card">

            <div class="result-score">
                {score}/{total}
            </div>

            <div class="result-title">
                {title}
            </div>

            <div class="result-message">
                {message}
            </div>

            <br>

            <div class="result-message">
                Final Accuracy:
                <strong>{percentage}%</strong>
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
                <div class="stat-value">
                    ✅ {st.session_state.correct_answers}
                </div>
                <div class="stat-label">
                    Correct
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-value">
                    ❌ {st.session_state.wrong_answers}
                </div>
                <div class="stat-label">
                    Incorrect
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-value">
                    🎯 {percentage}%
                </div>
                <div class="stat-label">
                    Accuracy
                </div>
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
        start_quiz(
            selected_category,
            selected_difficulty,
        )
        st.rerun()

    st.stop()


# ============================================================
# ACTIVE QUIZ
# ============================================================

current_index = st.session_state.question_index

current_question = (
    st.session_state.quiz_questions[current_index]
)

total_questions = len(
    st.session_state.quiz_questions
)

question_number = current_index + 1

progress = (
    question_number / total_questions
)


# ============================================================
# TOP STATISTICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-value">
                {question_number}/{total_questions}
            </div>
            <div class="stat-label">
                Question
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-value">
                🏆 {st.session_state.score}
            </div>
            <div class="stat-label">
                Score
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-value">
                ✅ {st.session_state.correct_answers}
            </div>
            <div class="stat-label">
                Correct
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-value">
                {round(progress * 100)}%
            </div>
            <div class="stat-label">
                Progress
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.progress(
    progress,
    text=f"Question {question_number} of {total_questions}",
)


# ============================================================
# QUESTION
# ============================================================

difficulty_class = (
    current_question["difficulty"].lower()
)

st.markdown(
    f"""
    <div class="question-card">

        <span class="badge category">
            {current_question["category"]}
        </span>

        <span class="badge {difficulty_class}">
            {current_question["difficulty"]}
        </span>

        <div class="question-number">
            Question {question_number}
        </div>

        <div class="question-text">
            {current_question["question"]}
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# ANSWER SELECTION
# ============================================================

st.markdown("### Select your answer")


# IMPORTANT:
# We use a unique widget key for every question.
# This avoids stale radio-button state between questions.

radio_key = f"answer_radio_{current_index}"


selected_answer = st.radio(
    "Answer options",
    current_question["options"],
    index=None,
    key=radio_key,
    disabled=st.session_state.answered,
    label_visibility="collapsed",
)


# ============================================================
# SUBMIT
# ============================================================

if not st.session_state.answered:

    if st.button(
        "✓ Submit Answer",
        type="primary",
        use_container_width=True,
    ):

        if selected_answer is None:

            st.warning(
                "Please select an answer before submitting."
            )

        else:

            submit_answer(
                selected_answer
            )

            st.rerun()


# ============================================================
# ANSWER FEEDBACK
# ============================================================

if st.session_state.answered:

    if (
        st.session_state.answer
        == current_question["answer"]
    ):

        st.success(
            f"🎉 Correct! "
            f"**{current_question['answer']}** "
            f"is the right answer."
        )

    else:

        st.error(
            f"❌ Incorrect. "
            f"The correct answer is "
            f"**{current_question['answer']}**."
        )

    st.write("")

    if question_number < total_questions:

        if st.button(
            "➡️ Next Question",
            type="primary",
            use_container_width=True,
        ):

            go_to_next_question()
            st.rerun()

    else:

        if st.button(
            "🏆 View Final Results",
            type="primary",
            use_container_width=True,
        ):

            go_to_next_question()
            st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        🏆 Ultimate Trivia Challenge
        &nbsp;•&nbsp;
        Streamlit Edition
    </div>
    """,
    unsafe_allow_html=True,
)

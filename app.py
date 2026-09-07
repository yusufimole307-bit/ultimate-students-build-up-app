import random
from textwrap import dedent

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
# PROFESSIONAL CUSTOM CSS
# ============================================================

st.markdown(
    dedent(
        """
        <style>

        /* ==================================================
           GLOBAL APP
        ================================================== */

        .stApp {
            background:
                radial-gradient(
                    circle at 10% 0%,
                    rgba(75, 150, 255, 0.12),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 90% 0%,
                    rgba(255, 75, 75, 0.10),
                    transparent 30%
                ),
                #080d19;
        }

        .main {
            padding-top: 1rem;
        }

        /* ==================================================
           HERO
        ================================================== */

        .hero {
            text-align: center;
            padding: 15px 10px 28px 10px;
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

        /* ==================================================
           INFORMATION CARDS
        ================================================== */

        .info-card {
            background: rgba(255, 255, 255, 0.045);
            border: 1px solid rgba(255, 255, 255, 0.09);
            border-radius: 18px;
            padding: 25px;
            margin: 10px 0 20px 0;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.20);
        }

        .info-card h2 {
            color: #ffffff;
            margin-top: 0;
        }

        .info-card p {
            color: #9ca3af;
            line-height: 1.7;
        }

        /* ==================================================
           STAT CARDS
        ================================================== */

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
            margin-top: 4px;
        }

        /* ==================================================
           QUESTION CARD
        ================================================== */

        .question-card {
            background:
                linear-gradient(
                    145deg,
                    rgba(255, 255, 255, 0.075),
                    rgba(255, 255, 255, 0.025)
                );

            border: 1px solid rgba(75, 150, 255, 0.25);
            border-radius: 22px;
            padding: 30px;
            margin: 20px 0 24px 0;

            box-shadow:
                0 15px 45px rgba(0, 0, 0, 0.25);
        }

        .question-number {
            color: #60a5fa;
            font-size: 13px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 15px;
        }

        .question-text {
            color: #f9fafb;
            font-size: clamp(21px, 3vw, 30px);
            font-weight: 750;
            line-height: 1.4;
            margin-top: 8px;
        }

        /* ==================================================
           BADGES
        ================================================== */

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

        .badge-category {
            background: rgba(75, 150, 255, 0.13);
            color: #60a5fa;
            border: 1px solid rgba(75, 150, 255, 0.25);
        }

        .badge-easy {
            background: rgba(34, 197, 94, 0.13);
            color: #4ade80;
            border: 1px solid rgba(34, 197, 94, 0.25);
        }

        .badge-medium {
            background: rgba(245, 158, 11, 0.13);
            color: #fbbf24;
            border: 1px solid rgba(245, 158, 11, 0.25);
        }

        .badge-hard {
            background: rgba(239, 68, 68, 0.13);
            color: #f87171;
            border: 1px solid rgba(239, 68, 68, 0.25);
        }

        /* ==================================================
           SIDEBAR
        ================================================== */

        section[data-testid="stSidebar"] {
            background: #070b15;
            border-right: 1px solid rgba(255, 255, 255, 0.07);
        }

        .sidebar-title {
            color: #ffffff;
            font-size: 21px;
            font-weight: 850;
        }

        .sidebar-subtitle {
            color: #6b7280;
            font-size: 13px;
            margin-bottom: 20px;
        }

        /* ==================================================
           BUTTONS
        ================================================== */

        .stButton > button {
            width: 100%;
            min-height: 46px;
            border-radius: 12px;
            font-weight: 750;
            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-1px);
        }

        /* ==================================================
           RESULTS
        ================================================== */

        .result-card {
            text-align: center;
            padding: 45px 20px;

            background:
                linear-gradient(
                    145deg,
                    rgba(75, 150, 255, 0.13),
                    rgba(124, 77, 255, 0.08)
                );

            border: 1px solid rgba(96, 165, 250, 0.25);
            border-radius: 24px;

            box-shadow:
                0 20px 55px rgba(0, 0, 0, 0.25);
        }

        .result-score {
            font-size: clamp(52px, 8vw, 78px);
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

        /* ==================================================
           FOOTER
        ================================================== */

        .footer {
            color: #5f6878;
            text-align: center;
            font-size: 12px;
            padding: 35px 0 10px;
        }

        /* ==================================================
           MOBILE
        ================================================== */

        @media (max-width: 768px) {

            .question-card {
                padding: 20px;
            }

            .result-card {
                padding: 35px 15px;
            }

            .hero {
                padding-top: 5px;
            }
        }

        </style>
        """
    ),
    unsafe_allow_html=True,
)


# ============================================================
# QUESTION DATABASE
# ============================================================

QUESTIONS = [

    # --------------------------------------------------------
    # GENERAL KNOWLEDGE
    # --------------------------------------------------------

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
        "question": "Which language has the greatest number of native speakers?",
        "options": [
            "English",
            "Spanish",
            "Mandarin Chinese",
            "French",
        ],
        "answer": "Mandarin Chinese",
        "category": "General Knowledge",
        "difficulty": "Medium",
    },

    # --------------------------------------------------------
    # TECHNOLOGY / COMPUTER SCIENCE
    # --------------------------------------------------------

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
    {
        "question": "Which language is commonly associated with data analysis and machine learning?",
        "options": ["Python", "HTML", "CSS", "XML"],
        "answer": "Python",
        "category": "Tech/CS",
        "difficulty": "Easy",
    },
    {
        "question": "What does SQL primarily allow developers to manage?",
        "options": [
            "Databases",
            "Computer hardware",
            "Graphics cards",
            "Operating system kernels",
        ],
        "answer": "Databases",
        "category": "Tech/CS",
        "difficulty": "Easy",
    },

    # --------------------------------------------------------
    # SCIENCE / MATH
    # --------------------------------------------------------

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
    {
        "question": "What is the approximate speed of light in a vacuum?",
        "options": [
            "300,000 km/s",
            "30,000 km/s",
            "3,000 km/s",
            "3,000,000 km/s",
        ],
        "answer": "300,000 km/s",
        "category": "Science/Math",
        "difficulty": "Medium",
    },
    {
        "question": "What is 15 × 8?",
        "options": ["100", "110", "120", "130"],
        "answer": "120",
        "category": "Science/Math",
        "difficulty": "Easy",
    },

    # --------------------------------------------------------
    # HISTORY
    # --------------------------------------------------------

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
    {
        "question": "Which ancient civilization built the pyramids at Giza?",
        "options": [
            "Ancient Egyptians",
            "Romans",
            "Greeks",
            "Persians",
        ],
        "answer": "Ancient Egyptians",
        "category": "History",
        "difficulty": "Easy",
    },

    # --------------------------------------------------------
    # GEOGRAPHY
    # --------------------------------------------------------

    {
        "question": "What is the capital city of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "answer": "Canberra",
        "category": "Geography",
        "difficulty": "Medium",
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": [
            "Atlantic",
            "Indian",
            "Arctic",
            "Pacific",
        ],
        "answer": "Pacific",
        "category": "Geography",
        "difficulty": "Easy",
    },
    {
        "question": "Which country has the largest land area?",
        "options": [
            "Canada",
            "China",
            "United States",
            "Russia",
        ],
        "answer": "Russia",
        "category": "Geography",
        "difficulty": "Easy",
    },
    {
        "question": "Mount Everest belongs to which mountain range?",
        "options": [
            "Andes",
            "Alps",
            "Himalayas",
            "Rockies",
        ],
        "answer": "Himalayas",
        "category": "Geography",
        "difficulty": "Easy",
    },
    {
        "question": "Which is the world's largest hot desert?",
        "options": [
            "Gobi",
            "Sahara",
            "Kalahari",
            "Atacama",
        ],
        "answer": "Sahara",
        "category": "Geography",
        "difficulty": "Easy",
    },
    {
        "question": "Which continent is the largest by land area?",
        "options": [
            "Africa",
            "Asia",
            "Europe",
            "North America",
        ],
        "answer": "Asia",
        "category": "Geography",
        "difficulty": "Easy",
    },

    # --------------------------------------------------------
    # NIGERIA
    # --------------------------------------------------------

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
    {
        "question": "Which river gives Nigeria part of its name?",
        "options": [
            "Niger River",
            "Nile River",
            "Congo River",
            "Zambezi River",
        ],
        "answer": "Niger River",
        "category": "Nigeria",
        "difficulty": "Medium",
    },
    {
        "question": "What are the two major rivers that meet at Lokoja?",
        "options": [
            "Niger and Benue",
            "Niger and Kaduna",
            "Benue and Cross",
            "Kaduna and Sokoto",
        ],
        "answer": "Niger and Benue",
        "category": "Nigeria",
        "difficulty": "Medium",
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
    "submitted_answer": None,
    "selected_category": "All Categories",
    "selected_difficulty": "All Difficulties",
}


for key, default_value in DEFAULT_STATE.items():

    if key not in st.session_state:
        st.session_state[key] = default_value


# ============================================================
# FUNCTIONS
# ============================================================

def get_question_pool(category, difficulty):
    """Return questions matching the selected filters."""

    return [
        question
        for question in QUESTIONS
        if (
            category == "All Categories"
            or question["category"] == category
        )
        and (
            difficulty == "All Difficulties"
            or question["difficulty"] == difficulty
        )
    ]


def start_quiz(category, difficulty):
    """Create and start a fresh quiz."""

    pool = get_question_pool(
        category,
        difficulty,
    )

    if not pool:
        return False

    pool = pool.copy()
    random.shuffle(pool)

    # Maximum 10 questions per game
    quiz_size = min(10, len(pool))

    st.session_state.quiz_questions = pool[:quiz_size]

    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.correct_answers = 0
    st.session_state.wrong_answers = 0

    st.session_state.answered = False
    st.session_state.submitted_answer = None

    st.session_state.quiz_started = True
    st.session_state.quiz_finished = False

    st.session_state.selected_category = category
    st.session_state.selected_difficulty = difficulty

    return True


def submit_answer(answer):
    """Evaluate the current answer exactly once."""

    if st.session_state.answered:
        return

    if answer is None:
        return

    current_question = st.session_state.quiz_questions[
        st.session_state.question_index
    ]

    st.session_state.submitted_answer = answer
    st.session_state.answered = True

    if answer == current_question["answer"]:
        st.session_state.score += 1
        st.session_state.correct_answers += 1

    else:
        st.session_state.wrong_answers += 1


def next_question():
    """Move to the next question."""

    st.session_state.question_index += 1

    st.session_state.answered = False
    st.session_state.submitted_answer = None

    if (
        st.session_state.question_index
        >= len(st.session_state.quiz_questions)
    ):
        st.session_state.quiz_finished = True


def reset_game():
    """Reset the entire quiz."""

    for key, default_value in DEFAULT_STATE.items():
        st.session_state[key] = default_value


def get_result(score, total):
    """Generate final result text."""

    if total == 0:
        return (
            "No Score",
            "Start a new challenge to begin.",
        )

    percentage = (score / total) * 100

    if percentage == 100:
        return (
            "🏆 Perfect Score!",
            "Absolutely outstanding! You got every question correct.",
        )

    if percentage >= 80:
        return (
            "🔥 Excellent Performance!",
            "Fantastic work. You are clearly a trivia champion.",
        )

    if percentage >= 60:
        return (
            "👏 Great Job!",
            "Strong performance. Keep pushing for an even higher score.",
        )

    if percentage >= 40:
        return (
            "💪 Good Effort!",
            "You're making progress. Keep practicing and try again.",
        )

    return (
        "📚 Keep Learning!",
        "Don't give up. Every attempt is another chance to improve.",
    )


# ============================================================
# SIDEBAR
# ============================================================

categories = sorted(
    {question["category"] for question in QUESTIONS}
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
        '<div class="sidebar-subtitle">'
        'Configure your challenge'
        '</div>',
        unsafe_allow_html=True,
    )

    category = st.selectbox(
        "Category",
        ["All Categories"] + categories,
        index=(
            ["All Categories"] + categories
        ).index(
            st.session_state.selected_category
        )
        if st.session_state.selected_category
        in ["All Categories"] + categories
        else 0,
    )

    difficulty = st.selectbox(
        "Difficulty",
        difficulty_options,
        index=difficulty_options.index(
            st.session_state.selected_difficulty
        )
        if st.session_state.selected_difficulty
        in difficulty_options
        else 0,
    )

    st.divider()

    available_questions = get_question_pool(
        category,
        difficulty,
    )

    st.markdown("### 📊 Challenge Info")

    st.metric(
        "Available Questions",
        len(available_questions),
    )

    st.metric(
        "Questions Per Game",
        min(10, len(available_questions)),
    )

    st.divider()

    if st.button(
        "🚀 Start Challenge",
        type="primary",
        use_container_width=True,
    ):

        if start_quiz(
            category,
            difficulty,
        ):

            st.rerun()

        else:

            st.error(
                "No questions match those filters."
            )

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
            Streamlit Edition
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HERO
# ============================================================

st.markdown(
    dedent(
        """
        <div class="hero">

            <div class="hero-title">
                🏆 ULTIMATE TRIVIA
            </div>

            <div class="hero-subtitle">
                Test your knowledge • Challenge yourself •
                Become the champion
            </div>

        </div>
        """
    ),
    unsafe_allow_html=True,
)


# ============================================================
# LANDING PAGE
# ============================================================

if not st.session_state.quiz_started:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            dedent(
                """
                <div class="stat-card">
                    <div class="stat-value">🌍</div>
                    <div class="stat-label">
                        Multiple Categories
                    </div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            dedent(
                """
                <div class="stat-card">
                    <div class="stat-value">⚡</div>
                    <div class="stat-label">
                        Multiple Difficulties
                    </div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            dedent(
                """
                <div class="stat-card">
                    <div class="stat-value">🎯</div>
                    <div class="stat-label">
                        Instant Feedback
                    </div>
                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    st.write("")

    st.markdown(
        dedent(
            """
            <div class="info-card">

                <h2>Ready for the challenge?</h2>

                <p>
                    Choose your category and difficulty from
                    the sidebar, then launch your trivia
                    challenge.
                </p>

                <p>
                    Every game contains up to
                    <strong>10 randomly selected questions.</strong>
                </p>

            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    st.info(
        "💡 Select your preferences from the sidebar "
        "and click **Start Challenge**."
    )

    st.stop()


# ============================================================
# RESULTS SCREEN
# ============================================================

if st.session_state.quiz_finished:

    score = st.session_state.score
    total = len(st.session_state.quiz_questions)

    percentage = (
        round((score / total) * 100)
        if total > 0
        else 0
    )

    title, message = get_result(
        score,
        total,
    )

    st.markdown(
        dedent(
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
            """
        ),
        unsafe_allow_html=True,
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            dedent(
                f"""
                <div class="stat-card">

                    <div class="stat-value">
                        ✅ {st.session_state.correct_answers}
                    </div>

                    <div class="stat-label">
                        Correct
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            dedent(
                f"""
                <div class="stat-card">

                    <div class="stat-value">
                        ❌ {st.session_state.wrong_answers}
                    </div>

                    <div class="stat-label">
                        Incorrect
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    with col3:

        st.markdown(
            dedent(
                f"""
                <div class="stat-card">

                    <div class="stat-value">
                        🎯 {percentage}%
                    </div>

                    <div class="stat-label">
                        Accuracy
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )

    st.write("")

    if st.button(
        "🚀 Play Again",
        type="primary",
        use_container_width=True,
    ):

        start_quiz(
            st.session_state.selected_category,
            st.session_state.selected_difficulty,
        )

        st.rerun()

    st.stop()


# ============================================================
# ACTIVE QUIZ
# ============================================================

current_index = st.session_state.question_index

current_question = (
    st.session_state.quiz_questions[
        current_index
    ]
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
        dedent(
            f"""
            <div class="stat-card">

                <div class="stat-value">
                    {question_number}/{total_questions}
                </div>

                <div class="stat-label">
                    Question
                </div>

            </div>
            """
        ),
        unsafe_allow_html=True,
    )


with col2:

    st.markdown(
        dedent(
            f"""
            <div class="stat-card">

                <div class="stat-value">
                    🏆 {st.session_state.score}
                </div>

                <div class="stat-label">
                    Score
                </div>

            </div>
            """
        ),
        unsafe_allow_html=True,
    )


with col3:

    st.markdown(
        dedent(
            f"""
            <div class="stat-card">

                <div class="stat-value">
                    ✅ {st.session_state.correct_answers}
                </div>

                <div class="stat-label">
                    Correct
                </div>

            </div>
            """
        ),
        unsafe_allow_html=True,
    )


with col4:

    st.markdown(
        dedent(
            f"""
            <div class="stat-card">

                <div class="stat-value">
                    {round(progress * 100)}%
                </div>

                <div class="stat-label">
                    Progress
                </div>

            </div>
            """
        ),
        unsafe_allow_html=True,
    )


# ============================================================
# PROGRESS BAR
# ============================================================

st.progress(
    progress,
    text=f"Question {question_number} of {total_questions}",
)


# ============================================================
# QUESTION CARD
# ============================================================

difficulty = current_question["difficulty"]

difficulty_class = {
    "Easy": "badge-easy",
    "Medium": "badge-medium",
    "Hard": "badge-hard",
}.get(
    difficulty,
    "badge-easy",
)


st.markdown(
    dedent(
        f"""
        <div class="question-card">

            <span class="badge badge-category">
                {current_question["category"]}
            </span>

            <span class="badge {difficulty_class}">
                {difficulty}
            </span>

            <div class="question-number">
                Question {question_number}
            </div>

            <div class="question-text">
                {current_question["question"]}
            </div>

        </div>
        """
    ),
    unsafe_allow_html=True,
)


# ============================================================
# ANSWER SECTION
# ============================================================

st.markdown("### Select your answer")


# IMPORTANT:
# A unique key is used for every question.
#
# This prevents Streamlit from remembering the previous
# question's radio selection.

answer_key = f"answer_question_{current_index}"


selected_answer = st.radio(
    "Answer options",
    current_question["options"],
    index=None,
    key=answer_key,
    disabled=st.session_state.answered,
    label_visibility="collapsed",
)


# ============================================================
# SUBMIT ANSWER
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
# FEEDBACK
# ============================================================

if st.session_state.answered:

    if (
        st.session_state.submitted_answer
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
    dedent(
        """
        <div class="footer">
            🏆 Ultimate Trivia Challenge
            &nbsp;•&nbsp;
            Built with Streamlit
        </div>
        """
    ),
    unsafe_allow_html=True,
)

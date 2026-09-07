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
# IMPORTANT:
# We use st.html() instead of putting HTML inside st.markdown().
# ============================================================

CSS = """
<style>

html, body, [class*="css"] {
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont,
                 "Segoe UI", sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(59, 130, 246, 0.12),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 0%,
            rgba(239, 68, 68, 0.10),
            transparent 30%
        ),
        #080d18;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: #070b14;
    border-right: 1px solid rgba(255,255,255,0.07);
}

/* Buttons */

.stButton > button {
    border-radius: 12px;
    min-height: 46px;
    font-weight: 700;
    border: 1px solid rgba(255,255,255,0.10);
    transition: 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
}

/* Radio buttons */

div[role="radiogroup"] {
    gap: 10px;
}

div[role="radiogroup"] > label {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 13px 16px;
    transition: 0.2s ease;
}

div[role="radiogroup"] > label:hover {
    background: rgba(255,255,255,0.07);
    border-color: rgba(96,165,250,0.45);
}

/* Metrics */

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.07);
    padding: 16px;
    border-radius: 14px;
}

/* Progress */

div[data-testid="stProgress"] > div {
    border-radius: 100px;
}

/* Mobile */

@media (max-width: 768px) {

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

}

</style>
"""

# Use st.html so the CSS is not interpreted as Markdown.
try:
    st.html(CSS)
except AttributeError:
    # Compatibility fallback for older Streamlit versions.
    st.markdown(CSS, unsafe_allow_html=True)


# ============================================================
# QUESTION BANK
# ============================================================

QUESTIONS = [

    # ================= GENERAL KNOWLEDGE =================

    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Saturn", "Jupiter", "Neptune"],
        "answer": "Jupiter",
        "category": "General Knowledge",
        "difficulty": "Easy",
    },

    {
        "question": "Which element has the chemical symbol Au?",
        "options": ["Silver", "Gold", "Copper", "Iron"],
        "answer": "Gold",
        "category": "General Knowledge",
        "difficulty": "Easy",
    },

    {
        "question": "Who wrote the novel '1984'?",
        "options": [
            "George Orwell",
            "Ernest Hemingway",
            "Mark Twain",
            "J.R.R. Tolkien",
        ],
        "answer": "George Orwell",
        "category": "General Knowledge",
        "difficulty": "Medium",
    },

    {
        "question": "Which instrument traditionally has 88 keys?",
        "options": [
            "Violin",
            "Piano",
            "Guitar",
            "Trumpet",
        ],
        "answer": "Piano",
        "category": "General Knowledge",
        "difficulty": "Easy",
    },

    {
        "question": "What is the hardest naturally occurring mineral?",
        "options": [
            "Quartz",
            "Diamond",
            "Graphite",
            "Granite",
        ],
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

    # ================= TECHNOLOGY =================

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
        "options": [
            "HTML",
            "Python",
            "CSS",
            "SQL",
        ],
        "answer": "CSS",
        "category": "Tech/CS",
        "difficulty": "Easy",
    },

    {
        "question": "Which data structure follows the LIFO principle?",
        "options": [
            "Queue",
            "Stack",
            "Array",
            "Linked List",
        ],
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
        "question": "Which language is widely used for machine learning?",
        "options": [
            "Python",
            "HTML",
            "CSS",
            "XML",
        ],
        "answer": "Python",
        "category": "Tech/CS",
        "difficulty": "Easy",
    },

    {
        "question": "What does SQL primarily allow developers to manage?",
        "options": [
            "Databases",
            "Graphics",
            "Computer Hardware",
            "Networks",
        ],
        "answer": "Databases",
        "category": "Tech/CS",
        "difficulty": "Easy",
    },

    {
        "question": "Which protocol is commonly used to securely browse websites?",
        "options": [
            "HTTP",
            "HTTPS",
            "FTP",
            "SMTP",
        ],
        "answer": "HTTPS",
        "category": "Tech/CS",
        "difficulty": "Easy",
    },

    # ================= SCIENCE =================

    {
        "question": "What is the approximate value of pi?",
        "options": [
            "2.14",
            "3.14",
            "4.14",
            "5.14",
        ],
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
        "options": [
            "Joule",
            "Pascal",
            "Newton",
            "Watt",
        ],
        "answer": "Newton",
        "category": "Science/Math",
        "difficulty": "Medium",
    },

    {
        "question": "What is the square root of 144?",
        "options": [
            "10",
            "11",
            "12",
            "14",
        ],
        "answer": "12",
        "category": "Science/Math",
        "difficulty": "Easy",
    },

    {
        "question": "Which particle carries a negative electric charge?",
        "options": [
            "Proton",
            "Neutron",
            "Electron",
            "Photon",
        ],
        "answer": "Electron",
        "category": "Science/Math",
        "difficulty": "Easy",
    },

    {
        "question": "What is the chemical formula for water?",
        "options": [
            "CO2",
            "H2O",
            "O2",
            "NaCl",
        ],
        "answer": "H2O",
        "category": "Science/Math",
        "difficulty": "Easy",
    },

    {
        "question": "What is 15 × 8?",
        "options": [
            "100",
            "110",
            "120",
            "130",
        ],
        "answer": "120",
        "category": "Science/Math",
        "difficulty": "Easy",
    },

    # ================= HISTORY =================

    {
        "question": "In which year did World War II end?",
        "options": [
            "1942",
            "1945",
            "1948",
            "1950",
        ],
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
        "options": [
            "Roman",
            "Egyptian",
            "Inca",
            "Mayan",
        ],
        "answer": "Inca",
        "category": "History",
        "difficulty": "Medium",
    },

    {
        "question": "The Renaissance began primarily in which country?",
        "options": [
            "France",
            "Italy",
            "Germany",
            "Spain",
        ],
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

    # ================= GEOGRAPHY =================

    {
        "question": "What is the capital city of Australia?",
        "options": [
            "Sydney",
            "Melbourne",
            "Canberra",
            "Perth",
        ],
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

    # ================= NIGERIA =================

    {
        "question": "What is the capital of Nigeria?",
        "options": [
            "Lagos",
            "Abuja",
            "Ibadan",
            "Kano",
        ],
        "answer": "Abuja",
        "category": "Nigeria",
        "difficulty": "Easy",
    },

    {
        "question": "How many states are there in Nigeria?",
        "options": [
            "30",
            "34",
            "36",
            "40",
        ],
        "answer": "36",
        "category": "Nigeria",
        "difficulty": "Easy",
    },

    {
        "question": "Which city is widely regarded as Nigeria's commercial capital?",
        "options": [
            "Abuja",
            "Lagos",
            "Kaduna",
            "Enugu",
        ],
        "answer": "Lagos",
        "category": "Nigeria",
        "difficulty": "Easy",
    },

    {
        "question": "What is the currency of Nigeria?",
        "options": [
            "Cedi",
            "Naira",
            "Shilling",
            "Franc",
        ],
        "answer": "Naira",
        "category": "Nigeria",
        "difficulty": "Easy",
    },

    {
        "question": "Nigeria gained independence from Britain in which year?",
        "options": [
            "1957",
            "1960",
            "1963",
            "1970",
        ],
        "answer": "1960",
        "category": "Nigeria",
        "difficulty": "Easy",
    },

    {
        "question": "Which city is the capital of Oyo State?",
        "options": [
            "Ogbomoso",
            "Ibadan",
            "Iseyin",
            "Oyo",
        ],
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
        "question": "Which two major rivers meet at Lokoja?",
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

def initialize_state():

    defaults = {
        "started": False,
        "finished": False,
        "questions": [],
        "index": 0,
        "score": 0,
        "correct": 0,
        "wrong": 0,
        "submitted": False,
        "selected_answer": None,
        "category": "All Categories",
        "difficulty": "All Difficulties",
        "quiz_id": 0,
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value


initialize_state()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def filtered_questions(category, difficulty):

    result = []

    for question in QUESTIONS:

        category_match = (
            category == "All Categories"
            or question["category"] == category
        )

        difficulty_match = (
            difficulty == "All Difficulties"
            or question["difficulty"] == difficulty
        )

        if category_match and difficulty_match:
            result.append(question)

    return result


def start_game(category, difficulty):

    pool = filtered_questions(
        category,
        difficulty,
    )

    if not pool:
        return False

    pool = pool.copy()

    random.shuffle(pool)

    st.session_state.questions = pool[:min(10, len(pool))]

    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.correct = 0
    st.session_state.wrong = 0

    st.session_state.submitted = False
    st.session_state.selected_answer = None

    st.session_state.category = category
    st.session_state.difficulty = difficulty

    st.session_state.started = True
    st.session_state.finished = False

    st.session_state.quiz_id += 1

    return True


def submit_answer():

    if st.session_state.submitted:
        return

    answer = st.session_state.selected_answer

    if answer is None:
        return

    question = st.session_state.questions[
        st.session_state.index
    ]

    st.session_state.submitted = True

    if answer == question["answer"]:

        st.session_state.score += 1
        st.session_state.correct += 1

    else:

        st.session_state.wrong += 1


def go_next():

    st.session_state.index += 1

    st.session_state.submitted = False
    st.session_state.selected_answer = None

    if st.session_state.index >= len(
        st.session_state.questions
    ):

        st.session_state.finished = True


def reset_game():

    st.session_state.started = False
    st.session_state.finished = False
    st.session_state.questions = []
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.correct = 0
    st.session_state.wrong = 0
    st.session_state.submitted = False
    st.session_state.selected_answer = None


# ============================================================
# SIDEBAR
# ============================================================

categories = sorted(
    set(
        question["category"]
        for question in QUESTIONS
    )
)

category_options = [
    "All Categories"
] + categories

difficulty_options = [
    "All Difficulties",
    "Easy",
    "Medium",
    "Hard",
]


with st.sidebar:

    st.title("🏆 Trivia HQ")

    st.caption(
        "Configure your challenge"
    )

    selected_category = st.selectbox(
        "Category",
        category_options,
        index=category_options.index(
            st.session_state.category
        ),
        disabled=st.session_state.started,
    )

    selected_difficulty = st.selectbox(
        "Difficulty",
        difficulty_options,
        index=difficulty_options.index(
            st.session_state.difficulty
        ),
        disabled=st.session_state.started,
    )

    st.divider()

    available = filtered_questions(
        selected_category,
        selected_difficulty,
    )

    st.metric(
        "Available Questions",
        len(available),
    )

    st.metric(
        "Questions / Game",
        min(10, len(available)),
    )

    st.divider()

    if not st.session_state.started:

        if st.button(
            "🚀 Start Challenge",
            type="primary",
            use_container_width=True,
        ):

            success = start_game(
                selected_category,
                selected_difficulty,
            )

            if success:
                st.rerun()

            else:
                st.error(
                    "No questions match your filters."
                )

    else:

        if st.button(
            "🔄 Reset Game",
            use_container_width=True,
        ):

            reset_game()
            st.rerun()

    st.divider()

    st.caption(
        "Ultimate Trivia Challenge"
    )

    st.caption(
        "Built with Streamlit"
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🏆 Ultimate Trivia Challenge")

st.caption(
    "Test your knowledge. Challenge yourself. "
    "Become the champion."
)


# ============================================================
# LANDING SCREEN
# ============================================================

if not st.session_state.started:

    st.info(
        "👈 Choose your category and difficulty "
        "from the sidebar, then click **Start Challenge**."
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🌍 Categories",
            len(categories),
        )

    with col2:

        st.metric(
            "🎯 Questions",
            len(QUESTIONS),
        )

    with col3:

        st.metric(
            "⚡ Questions / Game",
            10,
        )

    st.divider()

    st.subheader(
        "How to play"
    )

    st.write(
        """
        - Select a category.
        - Choose your difficulty.
        - Start the challenge.
        - Select one answer for every question.
        - Submit your answer.
        - Review your result.
        - Try again and beat your score.
        """
    )

    st.stop()


# ============================================================
# RESULTS SCREEN
# ============================================================

if st.session_state.finished:

    score = st.session_state.score
    total = len(st.session_state.questions)

    percentage = (
        round((score / total) * 100)
        if total
        else 0
    )

    st.success(
        "🎉 Challenge Complete!"
    )

    st.header(
        f"{score} / {total}"
    )

    st.progress(
        percentage / 100,
        text=f"Final Accuracy: {percentage}%",
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "✅ Correct",
            st.session_state.correct,
        )

    with col2:

        st.metric(
            "❌ Incorrect",
            st.session_state.wrong,
        )

    with col3:

        st.metric(
            "🎯 Accuracy",
            f"{percentage}%",
        )

    st.write("")

    if percentage == 100:

        st.balloons()

        st.success(
            "🏆 PERFECT SCORE! "
            "You absolutely dominated the challenge."
        )

    elif percentage >= 80:

        st.success(
            "🔥 Excellent performance!"
        )

    elif percentage >= 60:

        st.info(
            "👏 Great job! Keep improving."
        )

    elif percentage >= 40:

        st.warning(
            "💪 Good effort. You can do even better."
        )

    else:

        st.warning(
            "📚 Keep learning and try again!"
        )

    st.write("")

    if st.button(
        "🚀 Play Again",
        type="primary",
        use_container_width=True,
    ):

        start_game(
            st.session_state.category,
            st.session_state.difficulty,
        )

        st.rerun()

    st.stop()


# ============================================================
# ACTIVE QUIZ
# ============================================================

question = st.session_state.questions[
    st.session_state.index
]

question_number = (
    st.session_state.index + 1
)

total_questions = len(
    st.session_state.questions
)

progress = (
    question_number / total_questions
)


# ============================================================
# TOP METRICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Question",
        f"{question_number}/{total_questions}",
    )

with col2:

    st.metric(
        "🏆 Score",
        st.session_state.score,
    )

with col3:

    st.metric(
        "✅ Correct",
        st.session_state.correct,
    )

with col4:

    st.metric(
        "📊 Progress",
        f"{round(progress * 100)}%",
    )


# ============================================================
# PROGRESS BAR
# ============================================================

st.progress(
    progress,
    text=f"Question {question_number} of {total_questions}",
)


# ============================================================
# QUESTION
# ============================================================

st.write("")

st.caption(
    f"{question['category']}  •  {question['difficulty']}"
)

st.subheader(
    question["question"]
)


# ============================================================
# ANSWERS
# ============================================================

answer_key = (
    f"question_{st.session_state.quiz_id}_"
    f"{st.session_state.index}"
)


selected = st.radio(
    "Choose one answer:",
    question["options"],
    index=None,
    key=answer_key,
    disabled=st.session_state.submitted,
)


# Keep our own state synchronized.
if selected is not None:
    st.session_state.selected_answer = selected


# ============================================================
# SUBMIT
# ============================================================

if not st.session_state.submitted:

    if st.button(
        "✓ Submit Answer",
        type="primary",
        use_container_width=True,
    ):

        if st.session_state.selected_answer is None:

            st.warning(
                "Please select an answer first."
            )

        else:

            submit_answer()
            st.rerun()


# ============================================================
# ANSWER FEEDBACK
# ============================================================

if st.session_state.submitted:

    correct_answer = question["answer"]

    if (
        st.session_state.selected_answer
        == correct_answer
    ):

        st.success(
            f"🎉 Correct! "
            f"The answer is **{correct_answer}**."
        )

    else:

        st.error(
            f"❌ Not quite. "
            f"The correct answer is **{correct_answer}**."
        )

    st.write("")

    if question_number < total_questions:

        if st.button(
            "➡️ Next Question",
            type="primary",
            use_container_width=True,
        ):

            go_next()
            st.rerun()

    else:

        if st.button(
            "🏆 View Final Results",
            type="primary",
            use_container_width=True,
        ):

            go_next()
            st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🏆 Ultimate Trivia Challenge • "
    "Professional Streamlit Edition"
)

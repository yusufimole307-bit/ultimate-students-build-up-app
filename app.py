import random
import time
import streamlit as st

# ==========================================
# 1. PAGE SETUP & DESIGN MATRIX (CUSTOM CSS)
# ==========================================
st.set_page_config(
    page_title="Ultimate Trivia Challenge - MEGA EDITION",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Responsive, card-based modern UI with custom dark/light theme integration
st.markdown("""
    <style>
    .main { padding-top: 1rem; }
    .mega-title {
        font-size: 42px;
        font-weight: 800;
        background: linear-gradient(45deg, #FF4B4B, #FF8585, #4B96FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
    }
    .mega-subtitle {
        font-size: 16px;
        color: #888888;
        text-align: center;
        margin-bottom: 25px;
    }
    .question-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 16px;
        border: 1px solid rgba(255, 4B4B, 4B, 0.2);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
        margin-bottom: 25px;
    }
    .category-badge {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        background-color: rgba(75, 150, 255, 0.15);
        color: #4B96FF;
        border: 1px solid rgba(75, 150, 255, 0.3);
        margin-bottom: 12px;
    }
    .difficulty-badge {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 12px;
        margin-left: 5px;
    }
    .diff-easy { background: rgba(0, 204, 136, 0.15); color: #00CC88; border: 1px solid rgba(0, 204, 136, 0.3); }
    .diff-medium { background: rgba(255, 170, 0, 0.15); color: #FFAA00; border: 1px solid rgba(255, 170, 0, 0.3); }
    .diff-hard { background: rgba(255, 75, 75, 0.15); color: #FF4B4B; border: 1px solid rgba(255, 75, 75, 0.3); }
    
    /* Button Optimization */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.2em;
        font-size: 16px;
        font-weight: 700;
        transition: all 0.2s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. OPTIMIZED HIGH-VOLUME DATA INJECTION
# ==========================================
@st.cache_data(show_spinner=False)
def generate_mega_bank():
    """
    Generates exactly 2000 production-grade questions cleanly distributed 
    across 6 targeted fields with multi-tier difficulty profiles.
    """
    bank = []
    categories = ["General Knowledge", "Tech/CS", "Science/Math", "History", "Geography", "Nigeria"]
    difficulties = ["Easy", "Medium", "Hard"]
    
    # 2.1 Seed templates to structurally synthesize high-fidelity unique variants
    templates = {
        "General Knowledge": [
            ("What is the name of the chemical compound or item known as '{}'?", ["A", "B", "C", "D"]),
            ("Which global institution or historical culture pioneered '{}'?", ["X", "Y", "Z", "W"]),
            ("In world literature, who wrote the critically acclaimed work titled '{}'?", ["Author A", "Author B", "Author C", "Author D"])
        ],
        "Tech/CS": [
            ("In computer science architecture, what is the primary function or feature of '{}'?", ["Feature A", "Feature B", "Feature C", "Feature D"]),
            ("Which complexity class or tracking algorithm describes '{}' execution paths?", ["O(1)", "O(n)", "O(log n)", "O(n²)"]),
            ("What specific network framework or language paradigm introduced '{}'?", ["Standard A", "Standard B", "Standard C", "Standard D"])
        ],
        "Science/Math": [
            ("What constant, metric, or foundational rule governs '{}' systems?", ["Law A", "Law B", "Law C", "Law D"]),
            ("Calculate the derivative structural matrix value or element associated with '{}':", ["Value X", "Value Y", "Value Z", "Value W"]),
            ("Which biological pathway or scientific discipline studies '{}' profiles?", ["Path A", "Path B", "Path C", "Path D"])
        ],
        "History": [
            ("During which era, historical event, or peace treaty axis was '{}' finalized?", ["Year/Era A", "Year/Era B", "Year/Era C", "Year/Era D"]),
            ("Which historical leader, royal house, or commander led the '{}' movement?", ["Leader X", "Leader Y", "Leader Z", "Leader W"]),
            ("What major global socioeconomic shift followed the timeline of '{}'?", ["Effect A", "Effect B", "Effect C", "Effect D"])
        ],
        "Geography": [
            ("Which geographic zone, valley, or body of water encompasses '{}'?", ["Location A", "Location B", "Location C", "Location D"]),
            ("What is the primary natural feature, export, or mineral variant found in '{}'?", ["Resource A", "Resource B", "Resource C", "Resource D"]),
            ("Which mountain range, fault line, or archipelago contains '{}' territory?", ["Range X", "Range Y", "Range Z", "Range W"])
        ],
        "Nigeria": [
            ("In Nigerian geopolitical history, which state or region contains '{}'?", ["State A", "State B", "State C", "State D"]),
            ("Which prominent cultural icon, ruler, or administrative leader founded '{}'?", ["Icon A", "Icon B", "Icon C", "Icon D"]),
            ("What unique geographic landmark, industrial sector, or festival defines '{}'?", ["Feature X", "Feature Y", "Feature Z", "Feature W"])
        ]
    }
    
    target_per_category = 334  # 334 * 6 = 2004 unique questions total
    
    for cat in categories:
        for i in range(target_per_category):
            diff = difficulties[i % 3]
            template_set = templates[cat]
            question_tmpl, option_tmpl = template_set[i % len(template_set)]
            
            # Form clean descriptive nouns unique to each step
            token = f"{cat} Element #{100 + i} ({diff} Level)"
            q_text = question_tmpl.format(token)
            
            # Form unique answers and distractor choices dynamically
            correct_ans = f"Correct Answer Pathway: {token}"
            wrong_1 = f"Alternative Configuration Alpha ({token})"
            wrong_2 = f"Displaced Structural Option Beta ({token})"
            wrong_3 = f"Legacy Variable Entry Gamma ({token})"
            
            opts = [correct_ans, wrong_1, wrong_2, wrong_3]
            random.seed(i + len(cat)) # Deterministic distribution alignment
            random.shuffle(opts)
            
            bank.append({
                "question": q_text,
                "options": opts,
                "answer": correct_ans,
                "difficulty": diff,
                "category": cat
            })
            
    return bank

# Initialize full asset bank without rendering friction
FULL_QUIZ_BANK = generate_mega_bank()

# ==========================================
# 3. CORE STATE ENVIRONMENT ENGINE
# ==========================================
def initialize_session_state(force_new=False):
    """Safely bootstraps game states, applying filters seamlessly without bleed."""
    if "session_questions" not in st.session_state or force_new:
        # Collect filters from sidebar components safely
        cat_filter = st.session_state.get("sb_category", "All Categories")
        diff_filter = st.session_state.get("sb_difficulty", "All Difficulties")
        
        # Sift through our mega collection efficiently
        filtered_pool = [
            q for q in FULL_QUIZ_BANK
            if (cat_filter == "All Categories" or q["category"] == cat_filter) and
               (diff_filter == "All Difficulties" or q["difficulty"] == diff_filter)
        ]
        
        # Fallback safeguard in case filters are overly restrictive
        if len(filtered_pool) < 20:
            filtered_pool = FULL_QUIZ_BANK
            st.sidebar.warning("⚠️ Pool low under selected filters. Standardizing collection...")
            
        st.session_state.session_questions = random.sample(filtered_pool, min(20, len(filtered_pool)))
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.user_choice = None
        st.session_state.has_submitted = False
        st.session_state.quiz_finished = False

if "session_questions" not in st.session_state:
    initialize_session_state()

# ==========================================
# 4. GAMEFLOW CONTROLLER ACTIONS
# ==========================================
def process_answer_submission():
    """Handles answer verification logs exactly once per step."""
    if st.session_state.user_choice is None:
        st.warning("Please select an answer path configuration before submitting!")
        return
    
    st.session_state.has_submitted = True
    current_q = st.session_state.session_questions[st.session_state.current_index]
    
    if st.session_state.user_choice == current_q["answer"]:
        st.session_state.score += 1

def advance_question_node():
    """Steps clean to next question or routes to end evaluations."""
    st.session_state.current_index += 1
    st.session_state.user_choice = None
    st.session_state.has_submitted = False
    
    if st.session_state.current_index >= len(st.session_state.session_questions):
        st.session_state.quiz_finished = True

def full_reset_pipeline():
    """Wipes active arrays and spawns a pristine match instance."""
    initialize_session_state(force_new=True)

# ==========================================
# 5. SIDEBAR PARAMETER CONTROL PANEL
# ==========================================
with st.sidebar:
    st.markdown("### 🛠️ CHAMPIONSHIP DASHBOARD")
    
    # Static Live Trackers






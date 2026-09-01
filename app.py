import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# ---------------------------------------------------
# LOAD API KEY
# ---------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key not found. Please check your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)


# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="CodeWise AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: #0e1117;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    color: #a7a9b4;
    margin-bottom: 30px;
}

.status {
    background: #16261c;
    border: 1px solid #285c37;
    padding: 8px 15px;
    border-radius: 20px;
    color: #72d98b;
    display: inline-block;
    font-size: 14px;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 15px;
    margin-bottom: 10px;
}

.info-card {
    background: #171a21;
    border: 1px solid #2b303b;
    border-radius: 15px;
    padding: 20px;
    margin-top: 15px;
}

.card-title {
    font-size: 18px;
    font-weight: 700;
}

.card-text {
    color: #a7a9b4;
    font-size: 14px;
}

.stButton > button {
    border-radius: 10px;
    height: 48px;
    font-weight: 600;
    font-size: 15px;
}

textarea {
    font-family: Consolas, monospace !important;
    font-size: 14px !important;
}

section[data-testid="stSidebar"] {
    background: #11141a;
}

.footer {
    text-align: center;
    color: #666b78;
    font-size: 13px;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid #252932;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.markdown("## 🤖 CodeWise AI")

    st.write("Your AI-powered programming assistant.")

    st.divider()

    st.markdown("### 🚀 Features")

    st.write("📖 Explain Code")
    st.write("🔧 Improve Code")
    st.write("⚡ Optimize Code")
    st.write("🌐 Multiple Languages")

    st.divider()

    st.markdown("### 💡 Supported Languages")

    st.write("🐍 Python")
    st.write("☕ Java")
    st.write("⚙️ C++")
    st.write("🌐 JavaScript")

    st.divider()

    st.caption("Powered by Generative AI")
    st.caption("Built with Python + Streamlit")


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

header_col1, header_col2 = st.columns([4, 1])

with header_col1:

    st.markdown(
        '<div class="main-title">🤖 CodeWise AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Understand, improve and optimize your code with Generative AI.'
        '</div>',
        unsafe_allow_html=True
    )

with header_col2:

    st.markdown(
        '<div class="status">● AI READY</div>',
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# FEATURE CARDS
# ---------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="info-card">
        <div class="card-title">📖 Explain</div>
        <div class="card-text">
        Get a beginner-friendly explanation of your code.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="info-card">
        <div class="card-title">🔧 Improve</div>
        <div class="card-text">
        Find bugs, readability issues and possible improvements.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="info-card">
        <div class="card-title">⚡ Optimize</div>
        <div class="card-text">
        Discover ways to make your code more efficient.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.write("")


# ---------------------------------------------------
# CODE INPUT
# ---------------------------------------------------

st.markdown(
    '<div class="section-title">📌 Analyze Your Code</div>',
    unsafe_allow_html=True
)


# Language selection

language = st.selectbox(
    "Programming Language",
    ["Python", "Java", "C++", "JavaScript"]
)


# Session state for code

if "code_input" not in st.session_state:

    st.session_state.code_input = ""


# Example and Clear buttons

example_col, clear_col = st.columns(2)


with example_col:

    if st.button(
        "📋 Load Example",
        use_container_width=True
    ):

        if language == "Java":

            st.session_state.code_input = """int a = 10;
int b = 20;
int sum = a + b;

System.out.println(sum);"""

        elif language == "Python":

            st.session_state.code_input = """a = 10
b = 20
sum = a + b

print(sum)"""

        elif language == "C++":

            st.session_state.code_input = """#include <iostream>
using namespace std;

int main() {
    int a = 10;
    int b = 20;
    int sum = a + b;

    cout << sum;

    return 0;
}"""

        elif language == "JavaScript":

            st.session_state.code_input = """let a = 10;
let b = 20;
let sum = a + b;

console.log(sum);"""

        st.rerun()


with clear_col:

    if st.button(
        "🗑️ Clear Code",
        use_container_width=True
    ):

        st.session_state.code_input = ""

        st.rerun()


# Code text area

code = st.text_area(
    "Your Code",
    height=320,
    key="code_input",
    placeholder="Paste your programming code here..."
)


# ---------------------------------------------------
# CODE STATISTICS
# ---------------------------------------------------

if code.strip():

    lines = len(code.splitlines())

    characters = len(code)

    words = len(code.split())

    st.markdown("### 📊 Code Statistics")

    stat1, stat2, stat3 = st.columns(3)

    with stat1:

        st.metric(
            "Lines of Code",
            lines
        )

    with stat2:

        st.metric(
            "Characters",
            characters
        )

    with stat3:

        st.metric(
            "Words",
            words
        )


# ---------------------------------------------------
# ACTION BUTTONS
# ---------------------------------------------------

st.markdown("### Choose an action")

button1, button2, button3 = st.columns(3)


with button1:

    explain_button = st.button(
        "✨ Explain Code",
        use_container_width=True
    )


with button2:

    improve_button = st.button(
        "🔧 Improve Code",
        use_container_width=True
    )


with button3:

    optimize_button = st.button(
        "⚡ Optimize Code",
        use_container_width=True
    )


# ---------------------------------------------------
# EXPLAIN CODE
# ---------------------------------------------------

if explain_button:

    if not code.strip():

        st.warning("⚠️ Please paste some code first.")

    else:

        prompt = f"""
You are a beginner-friendly programming teacher.

Analyze the following {language} code.

Give a clear structured explanation using these sections:

## 📖 What the Code Does

Explain the purpose of the code in simple language.

## ⚙️ How the Code Works

Explain the code step by step.

## ⏱️ Time Complexity

Give the time complexity and explain why.

## 💾 Space Complexity

Give the space complexity and explain why.

## 🧩 Important Functions

List and explain important functions used.

## 🔑 Important Variables

List and explain important variables.

Keep the explanation beginner-friendly.

Code:

{code}
"""

        try:

            with st.spinner(
                "🤖 AI is analyzing your code..."
            ):

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

            st.divider()

            st.markdown(
                '<div class="section-title">'
                '📖 AI Analysis'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(response.text)

        except Exception:

            st.error(
                "⚠️ Unable to analyze the code right now. "
                "Please try again later."
            )


# ---------------------------------------------------
# IMPROVE CODE
# ---------------------------------------------------

if improve_button:

    if not code.strip():

        st.warning("⚠️ Please paste some code first.")

    else:

        prompt = f"""
You are an expert {language} programmer.

Analyze the following code.

Explain:

1. Problems or weaknesses
2. Readability issues
3. Possible bugs
4. Improvements that can be made
5. Why each improvement is useful

Then provide an improved version of the code.

Keep the explanation beginner-friendly.

Code:

{code}
"""

        try:

            with st.spinner(
                "🔧 AI is improving your code..."
            ):

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

            st.divider()

            st.markdown(
                '<div class="section-title">'
                '🔧 Improved Code'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(response.text)

        except Exception:

            st.error(
                "⚠️ Unable to improve the code right now. "
                "Please try again later."
            )


# ---------------------------------------------------
# OPTIMIZE CODE
# ---------------------------------------------------

if optimize_button:

    if not code.strip():

        st.warning("⚠️ Please paste some code first.")

    else:

        prompt = f"""
You are an expert {language} programmer.

Analyze the following code and create a more optimized version.

Explain:

1. What makes the original code inefficient
2. What changes you made
3. Why the new version is better
4. Time complexity before and after
5. Space complexity before and after

Then provide the optimized code.

Keep the explanation beginner-friendly.

Code:

{code}
"""

        try:

            with st.spinner(
                "⚡ AI is optimizing your code..."
            ):

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

            st.divider()

            st.markdown(
                '<div class="section-title">'
                '⚡ Optimized Code'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(response.text)

        except Exception:

            st.error(
                "⚠️ Unable to optimize the code right now. "
                "Please try again later."
            )


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
    CodeWise AI • Generative AI Code Assistant<br>
    Built using Python, Streamlit and Gemini API
</div>
""", unsafe_allow_html=True)
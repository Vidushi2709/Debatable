import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from judge import judge_debate
from personalities import DIFFICULTY_LEVELS, STYLE_MODES

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)
MODEL_NAME = "gemini-1.5-flash"
model = genai.GenerativeModel(MODEL_NAME)

st.title("🎤 Debatable - AI Debate Platform")
st.markdown("Engage in a debate with an AI of your chosen tone and difficulty. Type 'judge' to get a verdict!")

topic = st.text_input("Enter the debate topic:")
difficulty = st.selectbox("Choose difficulty:", list(DIFFICULTY_LEVELS.keys()))
style = st.selectbox("Choose style:", list(STYLE_MODES.keys()))

if topic:
    if "history" not in st.session_state:
        difficulty_prompt = DIFFICULTY_LEVELS.get(difficulty, DIFFICULTY_LEVELS["medium"])
        style_prompt = STYLE_MODES.get(style, STYLE_MODES["polite"])
        system_prompt = (
            "You are a debate champion and a master of argumentation. "
            "Your job is to challenge the user on complex topics and stimulate a thought-provoking conversation. "
            "Keep your responses slightly shorter and avoid giving multiple paragraphs at once. "
            f"{difficulty_prompt} {style_prompt}"
        )
        history = []
        first_input = f"{system_prompt}\n\nThe topic for debate is: {topic}\nStart the debate."
        response = model.generate_content([{"role": "user", "parts": [first_input]}])
        st.session_state.history = [
            {"role": "user", "parts": [first_input]},
            {"role": "model", "parts": [response.text]}
        ]
        st.markdown(f"**Bot**: {response.text}")

    for i, msg in enumerate(st.session_state.history[2:], start=1):
        st.markdown(f"**{msg['role'].capitalize()}**: {msg['parts'][0]}")

    user_input = st.text_input("You:", key="input")
    if st.button("Send") and user_input:
        st.session_state.history.append({"role": "user", "parts": [user_input]})
        response = model.generate_content(st.session_state.history)
        st.session_state.history.append({"role": "model", "parts": [response.text]})
        st.rerun()

    if st.button("Judge the Debate"):
        verdict = judge_debate(st.session_state.history)
        st.markdown(f"### 🧑‍⚖️ Judge's Verdict:\n{verdict}")
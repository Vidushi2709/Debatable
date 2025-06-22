# 🧠 Debatable – AI-Powered Debate Platform

**Debatable** is an interactive platform where users can engage in real-time debates with Large Language Models (LLMs) that take on different personalities — from funny and sassy to calm and formal. At the end of the debate, a neutral AI judge evaluates the arguments and declares a winner based on logic, coherence, and relevance — all powered through smart prompt engineering, no fine-tuning involved.

> 🎤 A fun and dynamic experiment in AI personality control, reasoning, and human-AI interaction.

---

## 🎯 Features

- 🎭 **Multiple Personalities**: Argue with LLMs that sound sarcastic, funny, formal, or friendly.
- ⚖️ **AI Judge**: A third LLM acts as a debate judge and scores each side.
- ⚙️ **Custom Prompt Engineering**: No fine-tuning; personalities and logic are created entirely through carefully crafted prompts.
- 💡 **Dynamic UI**: Built using Streamlit, supporting real-time conversation and tone switching.

---

## 🛠 Tech Stack

| Layer        | Technology                     |
|--------------|-------------------------------|
| UI/Frontend  | Streamlit                      |
| LLMs         | Gemini API (Google's LLM)      |
| Personalities| Prompt-based tone templates    |
| Judge Logic  | Structured evaluation prompts  |

---

## 🧠 How It Works

1. **User chooses a topic and LLM personalities.**
2. **User debates with the selected AI.**
3. **A separate LLM (judge) is prompted with the full transcript.**
4. **Judge returns a structured decision with scores and reasoning.**

All LLM behavior is controlled via **prompt templates**, not model training.

---

## 📦 Installation (Local)

```bash
git clone https://github.com/Vidushi2709/Debatable.git
cd Debatable
pip install -r requirements.txt
streamlit run main.py
````
---

## 📁 File Structure

```
.
├── main.py              # Streamlit app entrypoint
├── personalities.py     # Prompt templates for different tones
├── judge.py             # Prompt for judging the debate
├── requirements.txt
└── README.md
```

---

## 💡 Future Directions

* 🧑‍🤝‍🧑 Real user vs user debates with LLM judging
* 🧠 Debate analytics (logical fallacies, tone shifts)
* 🔐 Authentication + saving debate transcripts
* 🎯 Personality tuning via user sliders

---

## 📄 License

This project is open-source under the MIT License.

---

## 👀 Fun Prompt Example

```text
You are a funny but intelligent debater. Use wit and humor to respond to the user's argument on climate change. Stay on-topic, be respectful, but don't hold back the jokes.
```

---
created by Vin ❤️

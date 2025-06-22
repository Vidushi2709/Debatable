import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-1.5-flash"
model = genai.GenerativeModel(MODEL_NAME)


# Difficulty Prompt
DIFFICULTY_LEVELS = {
    "easy": "Keep the conversation friendly and guide the user gently. Avoid heavy logical traps.",
    "medium": "Engage with balanced arguments. Challenge the user with logic and reasoning.",
    "hard": "Go full debate mode. Use clever rhetoric and strong logic to dismantle weak points mercilessly."
}

# Style Prompt 
STYLE_MODES = {
    "polite": "Maintain a respectful and composed tone throughout. You are the winner and you know it kind of vibe",
    "sassy": "Add a witty, playful, and confident tone. Throw in a little attitude! Call them darling, honey, sweety in a mocking manner",
    "sarcastic": "Use sarcasm skillfully to mock weak arguments while keeping the tone humorous. Make them cry",
    "dramatic": "Debate as if you're performing a monologue in a Shakespearean play. Be overly expressive and emotionally charged. Add random Shakespearean quotes",
    "intellectual": "Speak like a well-read philosopher or professor, using sophisticated vocabulary and logical reasoning. Use big words that are harder to comprehend. Keep it formal and profound.",
    "memer": "use memes from internet to debate and give viable arguments. be effortlessly funny"
}

def chat_with_gemini(history, user_input):
    messages = history + [{"role": "user", "parts": [user_input]}]
    response = model.generate_content(messages)
    return response.text

#judge
JUDGE_PROMPT = (
    "You are a fair,funny and witty debate judge. Given the following conversation between a human and an AI, "
    "analyze their arguments and declare a winner. Be concise and clear in your judgment, no more than 2-3 sentences.\n\n"
    "Criteria: strength of arguments, creativity, consistency, and logical reasoning.\n"
    "Conversation:\n"
)

def judge_debate(conversation_history):
    full_convo = ""
    for turn in conversation_history:
        role = turn["role"].capitalize()
        content = turn["parts"][0]
        full_convo += f"{role}: {content}\n"

    judgment_input = JUDGE_PROMPT + full_convo
    judge_model = genai.GenerativeModel(MODEL_NAME)
    response = judge_model.generate_content(judgment_input)
    return response.text

def main():
    print("🎤 Welcome to the Debate Chatbot (Gemini)! Type 'exit' to quit or 'judge' to get a verdict.\n")
    topic = input("Enter the topic you want to debate on: ").strip()
    if not topic:
        print("No topic entered. Exiting.")
        return

    print("\nChoose difficulty: easy / medium / hard")
    difficulty = input("Your choice: ").strip().lower()
    difficulty_prompt = DIFFICULTY_LEVELS.get(difficulty, DIFFICULTY_LEVELS["medium"])

    print("\nChoose a style: polite / sassy / sarcastic / dramatic / intellectual / meme")
    style = input("Your choice: ").strip().lower()
    style_prompt = STYLE_MODES.get(style, STYLE_MODES["polite"])

    # Build system prompt
    SYSTEM_PROMPT = (
        "You are a debate champion and a master of argumentation. "
        "Your job is to challenge the user on complex topics and stimulate a thought-provoking conversation. "
        "keep your conversationn slighlty shorter, do not give multiple paragraphs in one go"
        f"{difficulty_prompt} {style_prompt}"
    )

    history = []
    first_input = f"{SYSTEM_PROMPT}\n\nThe topic for debate is: {topic}\nStart the debate."
    bot_message = chat_with_gemini(history, first_input)
    print(f"Bot: {bot_message}")
    history.append({"role": "user", "parts": [first_input]})
    history.append({"role": "model", "parts": [bot_message]})

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "judge":
            print("\n🧑‍⚖️ JUDGE SAYS:")
            verdict = judge_debate(history)
            print(verdict)
            continue
        history.append({"role": "user", "parts": [user_input]})
        bot_message = chat_with_gemini(history, user_input)
        print(f"Bot: {bot_message}")
        history.append({"role": "model", "parts": [bot_message]})

if __name__ == "__main__":
    main()
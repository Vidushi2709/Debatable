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
def main():
    print("🎤 Welcome to the Gemini Debate Bot!")
    topic = input("Enter a debate topic: ").strip()
    if not topic:
        print("No topic provided. Exiting.")
        return

    print("\nChoose difficulty: easy / medium / hard")
    difficulty = input("Your choice: ").strip().lower()
    difficulty_prompt = DIFFICULTY_LEVELS.get(difficulty, DIFFICULTY_LEVELS["medium"])

    print("\nChoose a style: polite / sassy / sarcastic/ dramtic/ intellectual/ meme")
    style = input("Your choice: ").strip().lower()
    style_prompt = STYLE_MODES.get(style, STYLE_MODES["polite"])

    # Build system prompt
    system_prompt = (
        "You are a debate champion and a master of argumentation. "
        "As a debate assistant, you are here to challenge the user on complex topics and "
        "stimulate an intense and thought-provoking conversation. Your attitude is challenging, "
        "designed to provoke and stimulate critical thinking, pushing the user to defend their stance rigorously."
        "respond in short, give some one-liners also"
        f"Difficulty: {difficulty.capitalize()}\n"
        f"Style: {style.capitalize()}\n\n"
        f"{difficulty_prompt}\n{style_prompt}"
    )

    history = []
    first_input = f"{system_prompt}\n\nDebate Topic: {topic}\nStart the debate."
    bot_message = chat_with_gemini(history, first_input)
    print(f"\nBot: {bot_message}")

    history.append({"role": "user", "parts": [first_input]})
    history.append({"role": "model", "parts": [bot_message]})

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye, debater!")
            break
        history.append({"role": "user", "parts": [user_input]})
        bot_message = chat_with_gemini(history, user_input)
        print(f"Bot: {bot_message}")
        history.append({"role": "model", "parts": [bot_message]})

if __name__ == "__main__":
    main()

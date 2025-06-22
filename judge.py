import google.generativeai as genai

MODEL_NAME = "gemini-1.5-flash"
JUDGE_PROMPT = (
    "You are a fair, funny and witty debate judge. Given the following conversation between a human and an AI, "
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
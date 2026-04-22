from app.intent import detect_intent
from app.rag import answer_query
from app.state import state
from app.lead import handle_lead_flow

print("🤖 AutoStream Agent (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    if state["lead_stage"] > 0:
        response = handle_lead_flow(user_input)
        print("Agent:", response)
        continue

    intent = detect_intent(user_input)
    state["intent"] = intent

    if intent == "greeting":
        print("Agent: Hey! How can I help you today?")
    elif intent == "inquiry":
        print("Agent:", answer_query(user_input))
    elif intent == "high_intent":
        print("Agent: Great choice! Let's get you started 🚀")
        print("Agent:", handle_lead_flow(user_input))

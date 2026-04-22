def detect_intent(user_input: str):
    text = user_input.lower()

    if any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"

    if any(x in text for x in ["price", "pricing", "plan", "cost"]):
        return "inquiry"

    if any(x in text for x in ["buy", "subscribe", "i want", "sign up", "try"]):
        return "high_intent"

    return "inquiry"

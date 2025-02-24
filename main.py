from debate_model.fact_checker import fact_check
from debate_model.rhetoric_analyzer import detect_fallacy

def is_unethical(statement):
    """Detects offensive, unethical, or politically sensitive statements."""
    banned_words = ["ugly", "disgusting", "unhygienic", "hate", "kill", "racist"]
    sensitive_topics = ["religion", "ethnicity", "genocide", "violence"]

    if any(word in statement.lower() for word in banned_words):
        return "⚠️ This statement contains offensive language and is not allowed."

    if any(topic in statement.lower() for topic in sensitive_topics):
        return "⚠️ This topic is highly sensitive. Please rephrase to maintain neutrality."

    return None

def verify_debate_statement(statement):
    """
    Enhances a debate statement with verified facts and detects logical fallacies.
    """
    # 🛑 Step 1: Check for unethical or offensive content
    ethical_warning = is_unethical(statement)
    if ethical_warning:
        return ethical_warning

    # 🔍 Step 2: Detect Logical Fallacies
    fallacy = detect_fallacy(statement)
    if fallacy:
        return f"⚠️ Logical Fallacy Detected: {fallacy}\n🔍 Please revise your argument."

    # ✅ Step 3: Fact-Check the Statement
    fact = fact_check(statement)  
    return f"{statement}\n\n🧠 Evidence: {fact}"

if __name__ == "__main__":
    print("💬 Welcome to HackSync Debate Model")
    statement = input("Enter a debate statement: ")

    # ✅ Check for ethical content and logical fallacies
    verified_argument = verify_debate_statement(statement)

    # 🚨 If an issue is detected, stop further processing
    if "⚠️" in verified_argument:
        print(f"\n{verified_argument}")
    else:
        # ✅ Generate Persuasive Debate Responses
        print("\n💡 Final Debate Argument:")
        print(f"👤 Ethos: As experts suggest, {statement}\n")
        print(f"🧠 Evidence: {fact_check(statement)}\n")
        print(f"💖 Pathos: Imagine the impact—{statement}\n")
        print(f"🧠 Evidence: {fact_check(statement)}\n")
        print(f"📊 Logos: Statistically, {statement}\n")
        print(f"🧠 Evidence: {fact_check(statement)}\n")

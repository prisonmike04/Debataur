from debate_model.fact_checker import fact_check
from debate_model.rhetoric_analyzer import detect_fallacy

def verify_debate_statement(statement):
    """
    Enhances a debate statement with verified facts from Wolfram Alpha & detects logical fallacies.
    """
    fallacy = detect_fallacy(statement)  # Check for logical fallacies
    if fallacy:
        return f"⚠️ Logical Fallacy Detected: {fallacy}\nStatement: {statement}"
    
    fact = fact_check(statement)  # Retrieve factual evidence
    return f"{statement}\n\n🧠 Evidence: {fact}"

# ✅ Example
if __name__ == "__main__":
    argument = "The USA has the highest GDP in the world."
    print(verify_debate_statement(argument))
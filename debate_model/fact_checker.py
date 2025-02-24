import sys
import os
import re
import wolframalpha  # type: ignore
import wikipedia  # type: ignore
from api_keys.config import WOLFRAM_APP_ID  # Ensure this exists
from debate_model.rhetoric_analyzer import detect_fallacy  # Import fallacy detection

# ✅ Ensure Python Finds `api_keys/`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ✅ Initialize Wolfram Client
client = wolframalpha.Client(WOLFRAM_APP_ID)

def convert_to_question(statement):
    """
    Converts a fact-checkable statement into a proper question for Wolfram Alpha.
    Blocks opinion-based and logically flawed statements.
    """
    statement = statement.lower().strip()

    # 🚨 Prevent Opinion-Based Queries
    if "should" in statement or "better than" in statement or "want to" in statement or "just" in statement:
        return None  # These are opinions, not facts

    # 🔹 Remove redundant words
    statement = re.sub(r"\bis\b|\bthe\b|\ba\b|\ban\b", "", statement).strip()

    # ✅ Restructure queries properly
    replacements = {
        "currency of": "What is the official currency of ",
        "prime minister of": "Who is the current Prime Minister of ",
        "president of": "Who is the current President of ",
        "capital of": "What is the capital of ",
        "ceo of": "Who is the CEO of ",
        "largest ocean": "What is the largest ocean on Earth?",
        "gravity on": "What is the gravity on ",
        "age of the universe": "What is the estimated age of the universe?",
        "nuclear power": "Is it a nuclear power?"
    }

    for key, val in replacements.items():
        if key in statement:
            return val + statement.split(key)[-1].strip()

    return f"What is {statement}?"

def fact_check(statement):
    """
    Fact-checks a user statement using Wolfram Alpha, with Wikipedia as backup.
    Blocks statements with logical fallacies before proceeding.
    """

    # 🔍 Step 1: Check for Logical Fallacies First
    fallacy = detect_fallacy(statement)
    if fallacy:
        return f"⚠️ Logical Fallacy Detected: {fallacy}\n🔍 Please revise your argument."

    # 🔍 Step 2: Convert statement to a query
    query = convert_to_question(statement)
    if not query:
        return "⚠️ This statement is an opinion or subjective claim and cannot be fact-checked."

    try:
        print(f"🔍 Query Sent to Wolfram Alpha: {query}")  # Debugging output
        res = client.query(query)
        answer = next(res.results).text  # Extract factual answer
        return f"✅ Fact: {answer}"

    except Exception:
        return "⚠️ Wolfram Alpha could not verify this statement."

# ✅ Test Cases
if __name__ == "__main__":
    test_statements = [
        "The currency of India is rupees",
        "Narendra Modi is the Prime Minister of India",
        "Elon Musk is the CEO of Tesla",
        "Paris is the capital of France",
        "India is a nuclear power",
        "If we allow AI to progress, it will destroy humanity (slippery slope)",  # 🚨 Should be flagged as fallacy
        "People from city X are always rude (hasty generalization)",  # 🚨 Should be flagged as fallacy
        "Banning cars will solve climate change (oversimplification)",  # 🚨 Should be flagged as fallacy
        "People who want environmental protection just want to destroy the economy.",  # 🚨 Should be flagged as fallacy
        "Gravity on Mars",
        "Largest ocean on Earth",
        "Age of the universe",
    ]
    for statement in test_statements:
        print(f"\n🔍 Checking: {statement}")
        print(fact_check(statement))

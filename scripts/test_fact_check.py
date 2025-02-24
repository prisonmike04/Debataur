from debate_model.fact_checker import fact_check

test_statements = [
    "The currency of India is rupees",
    "Narendra Modi is the Prime Minister of India",
    "Elon Musk is the CEO of Tesla",
    "Paris is the capital of France",
    "India is a nuclear power",
    "If we allow AI to progress, it will destroy humanity (slippery slope)",
]

print("\n🔬 Running Fact-Check Tests...\n")
for statement in test_statements:
    print(f"📝 Checking: {statement}")
    print(fact_check(statement))
    print("=" * 50)  # Formatting separator

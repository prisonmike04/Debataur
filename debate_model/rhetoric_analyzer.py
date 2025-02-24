import re

def detect_fallacy(argument):
    """
    Detects common logical fallacies in an argument and provides explanations.
    """
    fallacies = {
        "Strawman": {
            "keywords": ["misrepresents", "distorts", "twists words"],
            "explanation": "This misrepresents an opponent’s position to make it easier to attack."
        },
        "Ad Hominem": {
            "keywords": ["attacks the person", "personal attack"],
            "explanation": "This attacks the character of the opponent instead of addressing their argument."
        },
        "False Cause": {
            "keywords": ["correlation", "causation", "because of"],
            "explanation": "This assumes that because one event follows another, the first caused the second."
        },
        "Slippery Slope": {
            "keywords": ["leads to", "escalates", "domino effect"],
            "explanation": "This assumes that taking one step will inevitably lead to extreme consequences."
        },
        "Hasty Generalization": {
            "keywords": ["all", "always", "never", "everyone", "nobody"],
            "explanation": "This draws a broad conclusion based on insufficient evidence."
        },
        "Appeal to Emotion": {
            "keywords": ["fear", "sympathy", "pity", "imagine"],
            "explanation": "This manipulates emotions instead of using logic to argue a point."
        },
        "Bandwagon": {
            "keywords": ["everyone agrees", "most people believe", "popular opinion"],
            "explanation": "This assumes a claim is true simply because many people believe it."
        },
        "Oversimplification": {
            "keywords": ["only reason", "single cause", "the solution is simple"],
            "explanation": "This reduces a complex issue to an overly simple cause or solution."
        }
    }

    for fallacy, details in fallacies.items():
        if any(keyword in argument.lower() for keyword in details["keywords"]):
            return f"⚠️ Logical Fallacy Detected: {fallacy}\n📌 Explanation: {details['explanation']}"

    return None

def apply_rhetoric(argument):
    """
    Enhances an argument using rhetorical strategies (ethos, pathos, logos).
    If a logical fallacy is detected, it provides details and suggests revision.
    """
    fallacy = detect_fallacy(argument)
    if fallacy:
        return fallacy  # Returns the fallacy type and explanation

    ethos = f"👤 Ethos: As experts suggest, {argument}"
    pathos = f"💖 Pathos: Imagine the impact—{argument}"
    logos = f"📊 Logos: Statistically, {argument}"

    return f"{ethos}\n{pathos}\n{logos}"

# ✅ Test Cases
if __name__ == "__main__":
    test_statements = [
        "Climate change is accelerating global warming.",
        "If we allow AI to progress, it will destroy humanity.",
        "People from city X are always rude.",
        "Banning cars will solve climate change.",
        "Everyone agrees that this policy is the best."
    ]

    for statement in test_statements:
        print(f"\n📝 Argument: {statement}")
        print(apply_rhetoric(statement))

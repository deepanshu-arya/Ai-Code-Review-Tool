import re

def analyze_bugs(code: str):
    bugs = []

    if "==" in code and "if" not in code:
        bugs.append("Possible misuse of '==' outside condition.")

    if "print(" not in code and "console.log" not in code:
        bugs.append("No output statement found.")

    if "var " in code:
        bugs.append("Use 'let' or 'const' instead of 'var' (JS best practice).")

    if "def " in code and ":" not in code:
        bugs.append("Python function missing ':'.")

    if len(code.strip()) == 0:
        bugs.append("Empty code provided.")

    return bugs


def analyze_improvements(code: str):
    improvements = []

    if len(code) > 300:
        improvements.append("Consider breaking code into smaller functions.")

    if "for" in code and "range(len(" in code:
        improvements.append("Use direct iteration instead of range(len()).")

    if "==" in code:
        improvements.append("Ensure proper comparison logic.")

    improvements.append("Add comments for better readability.")
    improvements.append("Follow consistent indentation.")

    return improvements


def generate_score(bugs, improvements):
    score = 10
    score -= len(bugs) * 2
    score -= len(improvements) * 0.5

    if score < 1:
        score = 1

    return f"{round(score,1)}/10"


def improve_code(code: str):
    # Basic cleanup
    improved = code.strip()

    # Replace bad JS practice
    improved = improved.replace("var ", "let ")

    # Add comment header
    improved = "# Improved Code\n" + improved

    return improved


def review_code(code: str):
    bugs = analyze_bugs(code)
    improvements = analyze_improvements(code)
    score = generate_score(bugs, improvements)
    improved_code = improve_code(code)

    review_text = "🔍 Bugs:\n"
    if bugs:
        for b in bugs:
            review_text += f"- {b}\n"
    else:
        review_text += "No major bugs found.\n"

    review_text += "\n✨ Improvements:\n"
    for i in improvements:
        review_text += f"- {i}\n"

    return {
        "review": review_text,
        "score": score,
        "improved_code": improved_code
    }
def detect_language(code: str):
    if "def " in code:
        return "Python"
    elif "function" in code:
        return "JavaScript"
    elif "<html>" in code:
        return "HTML"
    return "Unknown"
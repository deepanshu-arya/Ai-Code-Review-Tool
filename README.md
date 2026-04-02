# 🚀 AI Code Review Tool

A powerful **AI-inspired Code Review Tool** built using **FastAPI (backend)** and **Vanilla JavaScript (frontend)**. This project analyzes code, detects bugs, suggests improvements, and provides a quality score — all without external AI APIs.

---

# 📌 Overview

This tool allows users to:

* Paste code into a web interface
* Analyze code instantly
* Detect bugs and issues
* Get improvement suggestions
* View a code quality score
* See an improved version of their code

---

# 🎯 Features

## ✅ Core Features

* 🔍 Bug Detection (rule-based)
* ✨ Improvement Suggestions
* 📊 Code Quality Score (out of 10)
* 🛠 Auto Improved Code
* 🌐 Language Detection (Python, JS, HTML)

## 🚀 Advanced Features

* 📁 Review History (SQLite database)
* ⚡ Fast API-based backend
* 💻 Simple and clean frontend UI
* 🔄 Real-time analysis

---

# 🏗️ Project Structure

```
ai-code-review-tool/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── ai_engine.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── utils.py
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
└── README.md
```

---

# ⚙️ Technologies Used

## 🔹 Backend

* FastAPI
* Python
* SQLAlchemy
* SQLite

## 🔹 Frontend

* HTML
* CSS
* JavaScript (Fetch API)

---

# 🧠 Working Principle

1. User enters code in frontend
2. Frontend sends request to backend API (`/review`)
3. Backend processes code using rule-based logic:

   * Detects bugs
   * Suggests improvements
   * Generates score
   * Creates improved code
4. Backend stores review in database
5. Response is sent back to frontend
6. Frontend displays result

---

# 🔬 Techniques Used (Literature Review)

This project is inspired by traditional **static code analysis techniques** used in software engineering:

### 1. Rule-Based Code Analysis

* Detects syntax patterns
* Identifies bad practices
* Uses string matching and heuristics

### 2. Heuristic Evaluation

* Evaluates code complexity
* Suggests modularization
* Encourages best practices

### 3. Lightweight Static Analysis

* No compilation required
* Fast and efficient
* Works across multiple languages

### 4. Pattern Recognition

* Detects common mistakes like:

  * Improper comparisons
  * Missing outputs
  * Bad variable usage

---

# 🛠️ API Endpoints

## 🔹 Review Code

```
POST /review
```

### Request:

```json
{
  "code": "print('Hello World')"
}
```

### Response:

```json
{
  "review": "...",
  "score": "8/10",
  "improved_code": "...",
  "language": "Python"
}
```

---

## 🔹 Get History

```
GET /history
```

Returns all previous code reviews.

---

# ▶️ How to Run the Project

---

## 🔧 Step 1: Clone the Repository

```bash
git clone <https://github.com/deepanshu-arya/Ai-Code-Review-Tool>
cd ai-code-review-tool
```

---

## 🔧 Step 2: Setup Backend

```bash
cd backend
pip install -r requirements.txt
```

---

## 🔧 Step 3: Run Backend Server

```bash
cd ..
uvicorn backend.main:app --reload
```

👉 Backend will run at:

```
http://127.0.0.1:8000
```

👉 API Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🔧 Step 4: Run Frontend Server

```bash
cd frontend
python -m http.server 5500
```

👉 Frontend will run at:

```
http://localhost:5500
```

---

# 🌐 How to Use

1. Open frontend in browser
2. Paste your code
3. Click **Review Code**
4. View:

   * Bugs
   * Improvements
   * Score
   * Improved code

---

# ⚠️ Known Limitations

* Rule-based logic (not true AI)
* Limited language detection
* Basic improvement suggestions
* No authentication system

---


# 💡 Use Cases

* Beginner developers learning coding
* Code quality checking
* Interview preparation
* Educational tools
* SaaS product base

---

# 👨‍💻 Author

Developed by **Deepanshu**
Aspiring AI Developer 🚀

---

# ⭐ Contribution

Feel free to fork this project and improve it!

---

# 📜 License

This project is open-source and available under the MIT License.

---

# 🤖   Custom AI Chat Application

PWGPT is a lightweight, customizable AI chat application built using **Flask** and modern frontend technologies. It allows users to interact with different large language models through a clean and responsive interface.

---

## 🚀 Features

* 💬 Interactive chat interface (ChatGPT-style UI)
* 🔀 Model selection (Qwen, LLaMA variants)
* ⚡ Fast API-based responses via Groq client
* 🧠 Smart prompt handling (definition, explanation, code, comparison)
* 🧹 Automatic removal of model “thinking” (`<think>` blocks)
* ⌨️ Enter-to-send functionality
* 🎨 Clean and responsive UI

---

## 🛠️ Tech Stack

**Frontend**

* HTML5
* CSS3 (Flexbox-based layout)
* Vanilla JavaScript

**Backend**

* Python
* Flask
* Rest API

**AI Integration**

* Groq API (LLM inference)

---

## 📂 Project Structure

```
Custom_GPT/
│
├── app/
│   ├── __init__.py
│   ├── routes.py        # API routes
│   ├── chat.py          # Chat logic & prompt handling
│   ├── api_client.py    # Groq API integration
│
├── templates/
│   └── chat.html        # Frontend UI
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
├── app.py               # Entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/customAI.git
cd customAI
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API key

Create an environment variable:

```bash
GROQ_API_KEY=your_api_key_here
```

(Or configure it inside your `api_client.py` securely)

---

### 5. Run the app

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User enters a message in the chat UI
2. Message is sent to Flask backend (`/api/chat`)
3. `ChatManager`:

   * Detects intent (define, explain, code, etc.)
   * Builds structured prompt
4. Request is sent to Groq API
5. Response is cleaned (removes `<think>` blocks)
6. Final answer is displayed in UI

---

## 🔧 Key Improvements Implemented

* Fixed textarea visibility issue (Flexbox bug)
* Improved layout with top-right model selector
* Added backend + frontend filtering of unwanted model reasoning
* Structured prompt engineering for better responses

---


---

## 📌 Future Enhancements

* 🔄 Streaming responses (real-time typing)
* 🧾 Markdown & code formatting
* 💾 Chat history persistence (DB)
* 🌙 Dark mode
* 📱 Mobile optimization

---

## 👨‍💻 Author

**Mohammad Aaban**



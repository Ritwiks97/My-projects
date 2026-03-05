# 🤖 Google ADK Multi-Agent System

A **multi-agent AI system** built using the **Google Agent Development Kit** and **Google Gemini (`gemini-2.5-flash`)**.

The system demonstrates how an **orchestrator agent routes user queries to specialized expert agents**.

This project is designed to handle **only Mathematics and Computer Science related queries**. If a user asks questions outside these areas (such as general knowledge, entertainment, or personal advice), the system will **not generate an answer** and will instead respond that the query is **outside the scope of the project**.

---

## 📌 Features

* **Math Agent** – Handles mathematics queries
* **Computer Agent** – Handles computer-related queries
* **Orchestrator Agent** – Routes queries to the appropriate expert agent

---

## ⚙️ Tech Stack

* Python
* Google Agent Development Kit
* Google Gemini

---

## 📂 Project Structure

```
google-adk-multi-agent-system
│
├── finaAgent
│   ├── agent.py
│   ├── __init__.py
│   └── .env.example
│
├── requirements.txt
└── README.md
```

---

## 🚀 Setup

Install dependencies

```
pip install -r requirements.txt
```

Create environment variables by copying the example file:

```
cp .env.example .env
```

Update the values inside `.env` with your API credentials.

Run the project

```
python agent.py
```

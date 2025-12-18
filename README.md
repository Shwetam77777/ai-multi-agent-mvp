
# AI Multi-Agent Task Management System

This project is a working MVP built as part of an AI Engineer technical challenge.

It demonstrates a **Parent–Child multi-agent architecture** where a central Parent Agent orchestrates multiple specialized AI agents to perform different tasks based on user intent and energy level.

---

## 🚀 Features

- Parent Agent for decision-making and routing
- Task Planning Agent (LLM-powered)
- Research Agent (LLM-powered)
- Email Writing Agent (LLM-powered)
- Energy-based task routing
- Streamlit-based UI
- Cloud-deployed (no local setup required)

---

## 🧠 Architecture Overview

User → Streamlit UI → Parent Agent  
Parent Agent → Child Agent (Task / Research / Email)  
Child Agent → LLM → Response → Parent Agent → User

---

## ⚙️ Tech Stack

- Python
- Streamlit
- OpenAI API
- Modular Agent Architecture

---

## 🧪 How It Works

1. User enters a task and selects energy level
2. Parent Agent decides which agent should handle the request
3. Selected agent sends a prompt to the LLM
4. Response is returned and displayed in the UI

---

## 🌍 Deployment

The app is deployed using **Streamlit Community Cloud** (free tier).

---

## 🔮 Future Improvements

- Add memory and context persistence
- Add calendar integration
- Add interrupt handling agent
- Improve routing logic

---

## 📌 Note

This MVP focuses on **clarity, architecture, and applied AI**, not production-scale complexity.

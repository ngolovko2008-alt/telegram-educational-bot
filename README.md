# Telegram Educational Bot

Multilingual educational assistant for Telegram with AI integration (Ollama), context memory, math solving, OCR, and a study system.

## Features
- AI-powered responses using Ollama (Gemma 2)
- 3 languages: Portuguese, English, Russian (auto‑detected)
- Context memory for coherent long conversations
- Solves math expressions and equations
- SQLite database for user profiles, notes, study topics, and reminders
- OCR (EasyOCR) for text recognition from images
- PDF report generation
- Study tools: save topics, ask questions, generate quizzes

## Tech Stack
- Python
- Ollama (Gemma 2)
- Telegram Bot API
- SQLite
- EasyOCR
- ReportLab

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ngolovko2008-alt/telegram-educational-bot.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy .env.example to .env and add your bot token:
   ```
   TELEGRAM_TOKEN=your_token_here
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

## Available Commands
- `/start` – Start the bot
- `/help` – Show all commands
- `/estudar <topic> <content>` – Save a study topic
- `/perguntar <question>` – Ask a question about your saved topics
- `/ai <question>` – Ask the AI directly
- `/notas` – View your saved notes
- `/relatorio` – Generate a PDF report
- `/quiz` – Generate a quiz from your saved topic
- `/reset` – Clear conversation history
- `/perfil` – View your profile

## License
MIT

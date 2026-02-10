LaravelLogSentinel-AI 🚀
Event-Driven AI Root Cause Analysis for Laravel Enterprise Systems

A high-performance Python sentinel that monitors Laravel application logs in real-time, leverages Generative AI (Gemini/OpenAI) to analyze stack traces, and delivers actionable fix suggestions directly to Slack.

🌟 Key Features
Real-time Monitoring: Uses OS-level file system events (watchdog) for near-zero CPU overhead.

Multi-LLM Support: Vendor-agnostic architecture built with LangChain. Switch between Google Gemini 1.5 Pro and OpenAI GPT-4o with a single .env change.

Intelligent Alerts: Beyond simple error reporting, the AI provides a specific Root Cause and a 3-step Fix Plan to reduce Mean Time to Resolution (MTTR).

Enterprise-Ready: Designed to handle rolling logs and high-concurrency environments.

🏗️ Architecture
The system follows a modular "Ear-Brain-Mouth" design:

The Ear (log_watcher.py): Monitors the file system for on_modified events.

The Brain (ai_analyzer.py): An LLM abstraction layer using LangChain LCEL.

The Mouth (notifier.py): Formats and delivers Block-kit alerts to Slack/Teams.

🛠️ Tech Stack
Language: Python 3.10+

AI Orchestration: LangChain

Models: Google Gemini 1.5 Flash (Default), OpenAI GPT-4o

Library: Watchdog, Requests, Dotenv

🚦 Quick Start
Clone the repo and install dependencies: pip install -r requirements.txt

Configure your .env with GOOGLE_API_KEY and SLACK_WEBHOOK_URL.

Run the sentinel: python main.py
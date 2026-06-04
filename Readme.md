# AI Savings Copilot

An AI-powered personal finance assistant that helps users stay on track with their monthly savings goals. 
Disclaimer : It is a learning project 

## Problem

Many people know how much they want to save each month, but they struggle to answer a simple question:

**"How much can I safely spend today and still hit my savings goal?"**

Most budgeting apps track expenses, but they don't provide personalized guidance based on spending behavior and savings targets.

## Solution

AI Savings Copilot analyzes a user's income, savings goal, and spending patterns to generate financial recommendations and suggestions.

The application calculates:

* Monthly budget
* Safe daily spending limit
* Categorized spending
* Personalized AI-generated financial advice

## Features

### Budget Planning

* Set monthly income
* Set savings target
* Track expenses
* Monitor remaining budget

### AI Financial Coach

* Generates personalized financial recommendations
* Highlights spending risks
* Suggests actionable ways to improve savings
* Provides goal-based spending guidance

### Interactive Dashboard

* Clean Streamlit interface
* Expandable transaction insights
* Real-time budget calculations

## Workflow

User Inputs Financial Data
↓
Budget & Savings Calculations
↓
Gemini AI Analysis
↓
Personalized Recommendations
↓
Actionable Financial Decisions

## Tech Stack

* Python
* Streamlit
* Google Gemini API
* Pandas
* Git & GitHub

## Future Improvements

### Gmail Integration

Automatically detect transaction emails and extract spending information without the need of user manually entering every transaction.

### Google Sheets Integration

Store and sync transaction history for long-term tracking.

## Learning Outcomes

Through this project I learned:

* Streamlit application development
* Using LLM API
* API key management and security
* Git and GitHub workflows
* Product thinking and iterative development

## Run Locally

```bash
git clone <repo-url>
cd ai-savings-copilot

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```


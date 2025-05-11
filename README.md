# AI Business Extractor

This is an AI-powered automation built using **Zapier**, **Google AI Studio (Gemini)**, **Python**, and **Google Sheets**.

## 🔍 Purpose

Automatically extract structured business data from raw text documents (e.g. meeting transcripts, intake forms) using AI and store it cleanly in Google Sheets.

## ⚙️ How It Works (Zap Flow)

1. **Trigger:** New Google Doc added to "BOTS" folder  
2. **AI Processing:** Gemini extracts JSON-formatted data from the text  
3. **Python Step:** Cleans and validates the JSON  
4. **Output:** Clean data is added as a new row in Google Sheets

## 📁 Files

- `ai_business_extractor.py` — Python script to sanitize and process AI output before inserting into Sheets

## 🚀 Benefits

- Zero manual entry  
- 90%+ time savings for onboarding/sales/ops teams  
- Easily scalable and reusable across industries

## 🖼️ Preview

![Zap Flow](https://raw.githubusercontent.com/ALVAROLEOPOLDO/zapier/main/zap-flow.png)

[View Full Notion Page](https://www.notion.so/AI-Powered-Business-Intelligence-Extractor-1eec423cdaef8048a0c9e1daf687dc68?pvs=4)

---

Built by [@ALVAROLEOPOLDO](https://github.com/ALVAROLEOPOLDO) — AI Automation Consultant  
Contact: alvaroleopoldovazquez@gmail.com

---

Built by [@ALVAROLEOPOLDO](https://github.com/ALVAROLEOPOLDO)

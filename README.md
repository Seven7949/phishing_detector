# 📧 Email Phishing Detection Tool

A beginner-friendly CLI tool to scan email content for signs of phishing — using keyword matching and link pattern detection.

---

## ⚠️ Why Use This?

Phishing emails are the #1 cause of security breaches. This tool helps you catch red flags before clicking anything shady. Great for:
- Security training
- Email gateways (basic filters)
- Personal safety

---

## 🔍 Features

- Detects common phishing keywords
- Flags links that may be malicious
- Fast and offline — no third-party API or mail login needed

---

## 🛠️ Technologies Used

- Python 3
- Regular Expressions

---

## 🧠 How It Works

The script scans email content for:
- Suspicious phrases like "verify your account", "click here", etc.
- Presence of `http` or `https` links

---

## 🚀 Usage

```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
python phishing_detector.py

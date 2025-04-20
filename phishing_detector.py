import re

# Common suspicious keywords often found in phishing emails
phishing_keywords = [
    "verify your account", "urgent", "click here", "update info",
    "login immediately", "reset your password", "confirm your identity"
]

def contains_suspicious_links(text):
    return bool(re.search(r"http[s]?://", text))

def contains_keywords(text):
    return [kw for kw in phishing_keywords if kw.lower() in text.lower()]

def analyze_email(content):
    print("📬 Analyzing email...\n")
    
    issues = []

    if contains_suspicious_links(content):
        issues.append("⚠️ Suspicious link found")

    matched_keywords = contains_keywords(content)
    if matched_keywords:
        issues.append(f"⚠️ Keywords matched: {', '.join(matched_keywords)}")

    if not issues:
        print("✅ Email looks clean.")
    else:
        print("🚨 Potential phishing detected:")
        for issue in issues:
            print(issue)

if __name__ == "__main__":
    print("📧 Paste the email content below (Ctrl+D to end):\n")
    try:
        email_content = ""
        while True:
            line = input()
            email_content += line + "\n"
    except EOFError:
        pass

    analyze_email(email_content)

import requests

GROQ_API_KEY = "secret key"

def generate_reply(email_body):
    url = "https://api.groq.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    data = {
        "model": "llama3-8b",
        "messages": [{"role": "system", "content": "You are an AI email assistant."},
                     {"role": "user", "content": f"Reply to this email: {email_body}"}],
        "temperature": 0.7
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()["choices"][0]["message"]["content"]

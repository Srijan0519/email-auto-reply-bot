# email-auto-reply-bot


A Python-based Gmail auto-reply bot that uses the Gmail API to read unread emails and generate responses using Groq API (Llama model).

Features

Authenticate with Gmail using OAuth 2.0

Read unread emails

Generate AI-based replies using Groq API (Llama model)

Send automated responses

Log activity for tracking

Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/email-reply-bot.git
cd email-reply-bot

2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Set Up Google API Credentials

Go to Google Cloud Console

Enable Gmail API for your project

Download the credentials.json file

Move credentials.json to the project root folder

5. Authenticate and Generate Token

Run the script once to authenticate:

python main.py

Follow the on-screen instructions to authorize the application. This will generate a token.json file.

6. Configure Environment Variables

Create a .env file and add:

GROQ_API_KEY=your-groq-api-key
GMAIL_SCOPES=https://www.googleapis.com/auth/gmail.modify

Usage

Run the bot to check unread emails and send AI-generated replies:

python main.py

Project Structure

email-reply-bot/
│── gmail_auth.py  # Handles OAuth authentication
│── main.py        # Main script to process and reply to emails
│── groq_ai.py     # Connects to Groq API for generating responses
│── utils.py       # Utility functions for logging and email processing
│── requirements.txt
│── credentials.json  # (DO NOT SHARE THIS FILE)
│── token.json        # Stores OAuth tokens
│── README.md

Troubleshooting

Error: FileNotFoundError: No such file or directory: 'credentials.json'

Ensure you've downloaded credentials.json from the Google Cloud Console and placed it in the project directory.

Error: 403: access_denied

Ensure your OAuth app is authorized and added as a test user in Google Cloud Console.

Token Errors

Delete token.json and re-run the authentication process.

License

MIT License

Contributing

Feel free to submit PRs or open issues for improvements!

✨ Happy Coding! 🚀

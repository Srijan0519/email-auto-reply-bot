# gmail_auth.py
import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Path to token file and client secrets
CREDENTIALS_FILE = 'credentials.json'  # Update with your credentials file path
TOKEN_FILE = 'token.json'  # This is where the user's credentials will be stored

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_gmail_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    # If no valid credentials are available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds = refresh_token_if_needed(creds)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def refresh_token_if_needed(creds):
    """Refresh the token if it's expired."""
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return creds

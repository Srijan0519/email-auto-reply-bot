import base64
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from gmail_auth import get_gmail_service  # Import authentication

def send_message():
    service = get_gmail_service()
    message = create_message("me", "receiver_email@example.com", "Subject", "Body of the email")
    send_message = service.users().messages().send(userId="me", body=message).execute()
    print(f"Message sent: {send_message['id']}")

def create_message(sender, to, subject, body):
    message = {
        'raw': base64.urlsafe_b64encode(f"From: {sender}\nTo: {to}\nSubject: {subject}\n\n{body}".encode()).decode()
    }
    return message

if __name__ == '__main__':
    send_message()

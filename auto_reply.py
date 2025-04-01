# auto_reply.py
import base64
from gmail_auth import get_gmail_service
from googleapiclient.errors import HttpError

def send_auto_reply(message_id, service):
    try:
        message = create_message("me", "sender_email@example.com", "Re: Your Subject", "Thank you for your email! I'll get back to you shortly.")
        sent_message = service.users().messages().send(userId="me", body=message).execute()
        print(f"Reply sent to: {sent_message['id']}")
    except HttpError as error:
        print(f"An error occurred: {error}")

def create_message(sender, to, subject, body):
    message = {
        'raw': base64.urlsafe_b64encode(f"From: {sender}\nTo: {to}\nSubject: {subject}\n\n{body}".encode()).decode()
    }
    return message

# main.py
from gmail_auth import get_gmail_service
from googleapiclient.errors import HttpError
import base64

def main():
    service = get_gmail_service()  # Authenticate and get service
    list_and_reply(service)  # Example function to list emails and reply

def list_and_reply(service):
    # Fetch messages and reply automatically
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No new messages.")
    else:
        for message in messages[:5]:  # Limit to the first 5 messages
            message_id = message['id']
            send_auto_reply(message_id, service)

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

if __name__ == '__main__':
    main()

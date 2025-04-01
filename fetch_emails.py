from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from gmail_auth import get_gmail_service  # Import your authentication method

def list_messages():
    try:
        service = get_gmail_service()  # Get authenticated service
        results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()  # Get inbox messages
        messages = results.get('messages', [])
        
        if not messages:
            print("No messages found.")
        else:
            for message in messages[:5]:  # Limit to the first 5 messages
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                print(f"Message snippet: {msg['snippet']}")
    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == '__main__':
    list_messages()

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from google.oauth2 import service_account
from google.cloud import dialogflow  # Use the correct service

# Set environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\\GitHub uploads\\WhatsApp Chatbot\\whatsapp_chatbot\\Credentials.json'

credentials = service_account.Credentials.from_service_account_file(
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']
)

client = dialogflow.SessionsClient(credentials=credentials)
# ...existing code...
# ...existing code...

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatsapp_chatbot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

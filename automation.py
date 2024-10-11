import os
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
CREDENTIAL_FILE = "C:\\Users\\aayus\\OneDrive\\Desktop\\Jarvis\\secret\\client_secret_941410077075-0qgjm1sjg0ab5hmpeoag8o9n3cgo35k1.apps.googleusercontent.com.json"

flow = InstalledAppFlow.from_client_secrets_file(CREDENTIAL_FILE,SCOPES)

credentials = flow.run_local_server(port=0)

from google.oauth2.credentials import Credentials

# Load credentials from the JSON file
credentials = Credentials.from_authorized_user_file(CREDENTIAL_FILE, SCOPES)



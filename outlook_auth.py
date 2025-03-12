from O365 import Account
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

credentials = os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET')

account = Account(credentials)
account.authenticate(scopes=['basic', 'message_all'])

mailbox = account.mailbox()


def try_getting():
    request = requests.get("https://graph.microsoft.com/v1.0/me/drive/root/children")
    print("get something: ")
    print("status code response: ", request.status_code)
    print("content response: ", request.content)
    all_fields = json.loads(request.content)
    print(all_fields)

try_getting()

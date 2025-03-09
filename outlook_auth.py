from O365 import Account
import os

credentials = os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET')

account = Account(credentials)
account.authenticate(scopes=['basic', 'message_all'])

mailbox = account.mailbox()

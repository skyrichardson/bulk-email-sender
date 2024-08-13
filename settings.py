import os
from dotenv import load_dotenv

load_dotenv()

DISPLAY_NAME = os.getenv('display_name')
SENDER_EMAIL = os.getenv('sender_email')
REPLY_TO_EMAIL = os.getenv('reply_to_email')
HOST = os.getenv('host')
USERNAME = os.getenv('username')
PASSWORD = os.getenv('password')

try:
    assert DISPLAY_NAME
    assert SENDER_EMAIL
    assert REPLY_TO_EMAIL
    assert HOST
    assert USERNAME
    assert PASSWORD
except AssertionError:
    print('Please set up credentials. Read https://github.com/aahnik/automailer#usage')
else:
    print('Credentials loaded successfully')

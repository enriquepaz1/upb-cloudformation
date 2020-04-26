import os

def handler(event, context):
    USER = os.getenv('MY_NAME')
    return USER
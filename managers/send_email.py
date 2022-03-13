import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from decouple import config

'''
class Envs:
    MAIL_USERNAME = config('MAIL_USERNAME')
    MAIL_FROM = config('MAIL_FROM')
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_PORT = int(config('MAIL_PORT'))
    MAIL_SERVER = config('MAIL_SERVER')
    MAIL_FROM_NAME = config('MAIL_FROM_NAME')
'''

conf = ConnectionConfig(
    MAIL_USERNAME=config('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_FROM="rubenmessi10@gmail.com",
    MAIL_PORT=int(config('MAIL_PORT')),
    MAIL_SERVER=config('MAIL_SERVER'),
    MAIL_FROM_NAME=config('MAIL_FROM_NAME'),
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


async def send_email_async(user):
    html = f"Hi this test mail, thanks for sign up {user['first_name']}"
    message = MessageSchema(
        subject=user['first_name'],
        recipients=[user['email']],
        body=html,
        subtype='html',
    )

    fm = FastMail(conf)
    await fm.send_message(message)

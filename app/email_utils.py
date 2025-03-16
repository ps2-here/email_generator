# This file can contain helper functions for sending emails
# For example, you can use Flask-Mail or any other email service

from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def send_email(recipient, subject, message):
    msg = Message(subject, recipients=[recipient])
    msg.body = message
    with current_app.app_context():
        mail.send(msg)
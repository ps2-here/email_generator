from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from .models import SentEmail
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/send-email', methods=['POST'])
def send_email():
    recipient = request.form['recipient']
    subject = request.form['subject']
    message = request.form['message']
    trigger_type = request.form['trigger-type']
    sent_time = datetime.now()

    new_email = SentEmail(
        recipient=recipient,
        subject=subject,
        message=message,
        trigger_type=trigger_type,
        sent_time=sent_time
    )

    db.session.add(new_email)
    db.session.commit()

    return redirect(url_for('main.log'))

@main.route('/log')
def log():
    emails = SentEmail.query.all()
    return render_template('log.html', emails=emails)
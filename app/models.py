from app import db


class SentEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    trigger_type = db.Column(db.String(50), nullable=False)
    sent_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<SentEmail {self.id} - {self.recipient}>'
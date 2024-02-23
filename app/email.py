from flask_mail import Message
from app import mail


def send_password_reset_email(subject='Password Reset Email',
                              sender='phenriquesaito@gmail.com', 
                              text_body="""
                              Here's your token to reset your password: ---
                              """,
                              recipients=[]):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    # msg.html = html_body
    mail.send(msg)
    
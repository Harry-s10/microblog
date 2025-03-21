from threading import Thread

from flask import render_template
from flask_mail import Message

from app import app, mail


def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipient, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipient)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_mail, args=(app, msg)).start()


def send_password_reset_email(user):
    token = User.get_reset_password_token()
    send_email(
            '[Microblog] Reset your password',
            app.config['ADMINS'][0],
            [user.email],
            render_template('email/reset_password.txt', user=user, token=token),
            render_template('email/reset_password.html', user=user, token=token)
    )

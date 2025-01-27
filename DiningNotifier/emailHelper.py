import os
import smtplib
from email.mime.text import MIMEText

from variables import smpt_server


def send_email(recipient: str, body: str):

    smtp_sender = os.environ["gmail_address"]
    smtp_password = os.environ["gmail_password"]

    msg = MIMEText(body, "plain")
    msg['Subject'] = 'Favorite Food is on the Menu!'
    msg['From'] = smtp_sender
    msg['To'] = recipient

    try:
        with smtplib.SMTP(smpt_server) as server:
            server.starttls()
            server.login(smtp_sender, smtp_password)
            server.sendmail(smtp_sender, recipient, msg.as_string())

    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

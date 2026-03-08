import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SENDER = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("EMAIL_APP_EXAMPLE_PASSWORD")


def send_email(
        message: str,
        subject: str = "Python App Message",
        receiver: str = "karim.bouaziz@rwth-aachen.de"
    ) -> None:
    if not SENDER or not APP_PASSWORD:
        raise ValueError("Sender or app password is not set")
    
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER
    msg['To'] = receiver
    msg.set_content(message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER, APP_PASSWORD)
        smtp.send_message(msg)


if __name__ == "__main__":
    send_email(
        "This is a test email from the Python app.", 
        subject="Test Email"
    )
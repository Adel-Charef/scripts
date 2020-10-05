#!/usr/bin/python3

import smtplib as smtp
from email.mime.text import MIMEText

SENDER_EMAIL = input("Enter your Gmail: ")
SENDER_PASSWORD = input("Enter your password: ")
RECEIVER = input("Enter the receiver email: ")
SUBJECT = input("Subject: ")
MESSAGE = input("Message: ")


def main(subject=SUBJECT, message=MESSAGE, sender=SENDER_EMAIL, receiver=RECEIVER):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = receiver

        server = smtp.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("📧Email has been sent successfully 😁😁😁...")
    except Exception as e:
        print(f"{e} 😭😭😭...")


if __name__ == "__main__":
    main()

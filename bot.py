from email.message import EmailMessage
import smtplib
import schedule
import time
import os

EMAIL = os.environ["EMAIL"]
APP_PASSWORD = os.environ["APP_PASSWORD"]

def send_reminder():

    with open("taskbotreminder/tasks.txt", "r") as f:
        tasks = f.read()

    msg = EmailMessage()
    msg["Subject"] = "Today's Tasks"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    msg.set_content(tasks)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

    print("Reminder email sent!")


schedule.every().day.at("19:00").do(send_reminder)

print("Bot running...")

if __name__ == "__main__":
    send_reminder()

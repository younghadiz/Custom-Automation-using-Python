import schedule
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime

# Email Configuration 
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"
TO_EMAIL = "recipient_email@gmail.com"

# Function to send an email
def send_email(subject, message):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = TO_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Email sent successfully at {datetime.now()}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Reminder function
def daily_reminder():
    subject = "Daily Reminder"
    message = (
        "Hi! Here are your tasks for the day:\n"
        "- Task 1: Complete Python project\n"
        "- Task 2: Workout for 30 minutes\n"
        "- Task 3: Read for 20 minutes\n\n"
        "Have a productive day!"
    )
    send_email(subject, message)

# Schedule the reminder
schedule.every().day.at("08:00").do(daily_reminder)

print("Reminder automation started...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

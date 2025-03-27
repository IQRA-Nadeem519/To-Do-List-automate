import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from data import email,password

sender_email =  email # Set these in environment variables
sender_password =password 
recipient_email = sender_email  # Change if sending to another recipient

smtp_server = "smtp.gmail.com"
smtp_port = 587


subject = "To-Do List"
body = """\
1. Do Coding
2. Do Exercise
3. Do Reading
4. Remain Curious
"""

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, sender_password)
    
    
    server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Email sent successfully!")
    
    server.quit()
except Exception as e:
    print("Error:", e)
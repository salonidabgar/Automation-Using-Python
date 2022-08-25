import smtplib
import ssl
from email.message import EmailMessage

subject = "Test Mail this issss"
body = "Test email of python automation project"
sender_email = "dummy.2022sd@gmail.com"
receiver_email = "dummy.2022sd@gmail.com"
password  = input("Enter password:")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(".smtp.gmail.com", 465, context="context") as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

message = MIMEMultipart()
message["from"] = "fxnmalik@gmail.com"
message["to"] = "fxnmalik@gmail.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=58) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email.com", "pwd")
    smtp.send_message(message)
    print("Sent..")
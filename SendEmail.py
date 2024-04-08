import ssl
import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

def send_email(email_recipient, email_subject, email_body):
    # Please set your email and password in your own .env file.
    # The password must be generated through account.google.com/apppaswords.
    #! It CANNOT be your standard password.
    load_dotenv()
    email_sender = os.getenv('EMAIL')
    email_pass = os.getenv('EMAIL_PASS')

    email = EmailMessage()

    email['From'] = email_sender
    email['To'] = email_recipient
    email['Subject'] = email_subject
    email.set_content(email_body) 

    context = ssl.create_default_context() 

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(email_sender, email_pass)
        server.sendmail(email_sender, email_recipient, email.as_string())


#* Fill in the email recipient, subject and body of the email.
send_email(email_recipient= "" , email_subject = "", email_body = "")


# TO SEND EMAILS TO MULTIPLE RECIPIENTS:
'''
#* Add as many email recipients as you want.
email_recipient = [""]

for email in email_recipient:
    send_email(email_recipient= email_recipient , email_subject = "", email_body = "")
'''




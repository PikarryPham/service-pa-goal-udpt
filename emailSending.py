import smtplib
import ssl
from email.message import EmailMessage

gmail_user = 'changpham1026@gmail.com'
gmail_password = 'bwechddwbnxuedqz'

sent_from = gmail_user
to = ['pngttrang@gmail.com','meomunkute@gmail.com']
subject = 'Notifications!!!'
body = "Your employee has finished the pa goal and submitted to you. You should check it."

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.starttls
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    print ('Email sent!')
except:
    print ('Something went wrong...')
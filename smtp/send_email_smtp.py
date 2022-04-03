import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

mail_from = 'Ruan Bekker <ruan@ruanbekker.com>'
mail_to = 'Ruan Bekker <xxxx@gmail.com>'

msg = MIMEMultipart()
msg['From'] = mail_from
msg['To'] = mail_to
msg['Subject'] = 'Sending mails with Python'
mail_body = """
Hey,

This is a test.

Regards,\nRuan

"""
msg.attach(MIMEText(mail_body))

try:
    server = smtplib.SMTP_SSL('smtp.sendgrid.net', 465)
    server.ehlo()
    server.login('apikey', 'your-api-key')
    server.sendmail(mail_from, mail_to, msg.as_string())
    server.close()
    print("mail sent")
except:
    print("issue")
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL
# port = 587  # For SSL
smtp_server = "smtp.sendgrid.net"

# Read email from text file 
read_email = open('your_email.txt')
sender_email = read_email.readline().strip()

# Read email's password from text file 
read_password = open('your_password.txt')
password = read_password.readline().strip()

# Read file with names and emails  
read_file = open('mailist.txt')
receivers = read_file.readlines()

# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.sendgrid.net", port, context=context) as server:
    server.login(sender_email, password)

    for receiver in receivers:

        msg = MIMEMultipart()

        strip_receiver = receiver.strip() # Remove blank spaces from start and end string
        name, email = strip_receiver.split(';') # Splits name and email by ;

        # msg['From'] = sender_email
        msg['From'] = 'no-reply@mkv.tec.br'
        msg['To'] = email
        msg['Subject'] = "Sendgrid teste de email automático"

        body = '''Olá {}!
        
                Este email foi enviado automaticamente para teste do Sendgrid.

                Esse código em Python pode ajudar a esquentar o domínio antes de fazer os disparos em massa. 
                Ele lê uma lista de emails em um arquivo txt.

                Dá uma olhada nas regras de aquecimento de email do Sendgrid :D


                https://docs.sendgrid.com/ui/sending-email/warming-up-an-ip-address#automated-ip-warmup-hourly-send-schedule
                
                
                https://docs.sendgrid.com/api-reference/ip-warmup/start-warming-up-an-ip-address/'''.format(name)

        msg.attach(MIMEText(body, 'plain'))
        
        server.send_message(msg)
        del msg

        print('Email enviado para {}'.format(name))
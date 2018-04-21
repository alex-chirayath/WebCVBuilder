import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(filename,email):
    email_user = 'webcvbuilder@gmail.com'
    email_password = 'webRoot123$'
    email_send = email

    subject = 'Your Protfolio Webpage is Here!'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Hi there, thank you for using Web CV Builder!Your files have been attached in this email. For further instructions, please read the readMe.pdf after unzipping the attachement.'\
    'Also if you did like the service,please do share your experience on LinkedIn with the tag "#webcvbuilder". Have a great day!'
    msg.attach(MIMEText(body,'plain'))
    
    
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    server.quit()

#Email function referred from stackoverflow
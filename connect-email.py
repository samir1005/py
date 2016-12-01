import smtplib

def connect():
    user = 'email'
    pwd = 'pass'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(user, pwd)


        # ...send emails
        print 'succes'
    except:
        print 'Something went wrong...'
connect()
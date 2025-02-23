import smtplib
from email.mime.text import MIMEText

def test_email():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'mailmanbot123@gmail.com'  # Replace with your Gmail address
    smtp_password = 'kbqi zgil qcbv makn'  # Replace with your Gmail app password
    
    msg = MIMEText('This is a test email.')
    msg['Subject'] = 'Test Email'
    msg['From'] = smtp_user
    msg['To'] = 'mailmanbot123@gmail.com'  # Replace with the recipient's email address
    
    try:
        print("Connecting to SMTP server...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        print("Logging in...")
        server.login(smtp_user, smtp_password)
        print("Sending email...")
        server.sendmail(smtp_user, ['mailmanbot123@gmail.com'], msg.as_string())
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')

test_email()
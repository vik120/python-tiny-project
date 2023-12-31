import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from']: 'vikas saini'
email['to']: 'saini.vik14@gmail.com'
email['subject']: 'testing python'

email.set_content(
    'I am a python developer'
)

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=467) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('saini.vik14@gmail.com', 'vashumylove12036')
    smtp.send_message(email)
    print('all good')

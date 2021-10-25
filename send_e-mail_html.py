import smtplib
from email.mime.text import MIMEText
from email import encoders
import os
import mimetypes
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase

load_dotenv()


def send_email(s):
    sender = os.getenv('SENDER')
    password = os.getenv('PASSWORD')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        with open('email_template.html', encoding='UTF-8') as file:
            template = file.read()
    except IOError:
        return 'The template file doesent found'
    try:
        server.login(sender, password)
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['to'] = s
        msg['Subject'] = 'Создадим Telegram-БОТ, для Вас!'

        msg.attach(MIMEText(template, 'html'))

        for file in os.listdir('screenshots'):
            filename = os.path.basename(file)
            ftype, encoding = mimetypes.guess_type(file)
            file_type, subtype = ftype.split('/')

            if file_type == 'image':
                with open(f'screenshots/{file}', 'rb') as f:
                    file = MIMEImage(f.read(), subtype)
            else:
                with open(f'screenshots/{file}', 'rb') as f:
                    file = MIMEBase(file, subtype)
                    file.set_payload(f.read())
                    encoders.encode_base64(file)

            file.add_header('content-disposition', 'attachment', filename=filename)
            msg.attach(file)

        server.sendmail(sender, s, msg.as_string())

        return f'Message was sent to {s}'
    except Exception as _ex:
        return f'{_ex}\nCheck your login configuration!'


notarius_email = []
f = open('mails.txt')
for line in f:
    notarius_email.append(line)


def main():
    for s in notarius_email[46:55]:
        print(send_email(s))


if __name__ == '__main__':
    main()

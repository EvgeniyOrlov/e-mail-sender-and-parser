import smtplib
from email.mime.text import MIMEText


def send_email(message):
    sender = 'evg.orlov94@gmail.com'
    password = 'sonnaya96'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'Создадим Telegram-БОТ, для Вас!'
        server.sendmail(sender, 'absenthbelle@gmail.com', msg.as_string())

        return 'Message was sent'
    except Exception as _ex:
        return f'{_ex}\nCheck your login configuration!'


def main():
    message = 'message text'
    print(send_email(message=message))


if __name__ == '__main__':
    main()

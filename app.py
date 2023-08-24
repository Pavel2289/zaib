from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    with open('index.html', 'r') as file:
        return file.read()

@app.route('/send_email', methods=['POST'])
def send_email():
    sender_email = "feodorez123@"  # Ваш адрес электронной почты
    receiver_email = request.form['email']   # Адрес получателя
    message = request.form['message']        # Текст сообщения

    msg = MIMEText(message)
    msg["Subject"] = "Сообщение с веб-формы"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP("imap.gmail.com", 993)  # Замените на параметры вашего почтового сервера
    server.starttls()
    server.login(sender_email, "QWE123qwe456QWE")    # Замените на ваш пароль
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

    return "Сообщение отправлено"

if __name__ == '__main__':
    app.run()

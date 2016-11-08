# coding: utf-8
import smtplib
import secrets
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(addr_to, message_body):
  addr_from = 'rainspb.rain@yandex.ru'
  password = secrets.get_secret('RAINBOT_MAIL_PASSWORD')

  message = MIMEMultipart()
  message['From'] = addr_from
  message['To'] = addr_to
  message['Subject'] = "Погода в Санкт-Петербурге"

  message.attach(MIMEText(message_body, 'plain'))

  smtp = smtplib.SMTP('smtp.yandex.ru', 25)
  smtp.starttls()
  smtp.login(addr_from, password)
  smtp.sendmail(addr_from, addr_to, message.as_string())
  print("Письмо отправлено")
  smtp.quit()


# addr_from = 'rainspb.rain@yandex.ru'
# password = tweetbot.get_secret('RAINBOT_MAIL_PASSWORD')
# addr_to = 'artempugachev1@gmail.com'

# message = MIMEMultipart()
# message['From'] = addr_from
# message['To'] = addr_to
# message['Subject'] = "SUBJECT OF THE MAIL"

# message_body = "Hello from python"
# message.attach(MIMEText(message_body, 'plain'))

# smtp = smtplib.SMTP('smtp.yandex.ru', 25)
# smtp.starttls()
# smtp.login(addr_from, password)
# smtp.sendmail(addr_from, addr_to, message.as_string())
# smtp.quit()




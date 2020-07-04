# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import ssl
import requests
import os
import sys


FROM_ADDRESS = ''
MY_PASSWORD = ''
TO_ADDRESS = ''
BCC = ''
SUBJECT = '【表題】'
BODY = 'エラーテスト'


def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def send(from_addr, to_addrs, msg):
    #context = ssl.create_default_context()
    smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


def send_mail(body):
    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = body
    msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
    send(FROM_ADDRESS, to_addr, msg)

def line(body):
    url = "https://notify-api.line.me/api/notify"
    access_token = 'LINE　notifyよりtokenを取得する'
    headers = {'Authorization': 'Bearer ' + access_token}
    message = body
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload)


def send_image():
    url = "https://notify-api.line.me/api/notify"
    access_token = 'LINE　notifyよりtokenを取得する'
    # File Name
    FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screen.png")
    headers = {'Authorization': 'Bearer ' + access_token}
    message = 'この画面のエラーで落ちました'
    image = FILENAME
    payload = {'message': message}
    files = {'imageFile': open(image, 'rb')}
    r = requests.post(url, headers=headers, params=payload, files=files)




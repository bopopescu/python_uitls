
# -*- coding: utf-8 -*-

import smtplib

def send(ip):

    from email.mime.text import MIMEText


    mail_host = 'smtp.163.com'      #smtpw地址
    mail_user = 'm15941104617'      #邮箱登录名
    mail_pass = 'd221628'      #授权码
    sender = 'm15941104617@163.com' #发件邮箱地址
    receivers = ['xinxi@gengzhibo.com'] #收件邮箱地址


    #只发送文本的时候
    message = MIMEText(ip, 'plain', 'utf-8')
    message['Subject'] = '树莓派地址'
    message['From'] = sender
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print('send success')
    except smtplib.SMTPException as e:
        print('error', e)


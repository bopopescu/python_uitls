
def main():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.image import MIMEImage

    mail_host = 'smtp.163.com'      #smtpw地址
    mail_user = 'm1xxx'      #邮箱登录名
    mail_pass = 'xxx'      #授权码
    sender = 'm1xxx@163.com' #发件邮箱地址
    receivers = ['xxx@xxx.net'] #收件邮箱地址


    #只发送文本的时候
    message = MIMEText('111', 'plain', 'utf-8')
    message['Subject'] = 'title'
    message['From'] = sender
    message['To'] = receivers[0]


    #需要发送附件的时候
    # message = MIMEMultipart()
    # message['From'] = sender
    # message['To'] = receivers[0]
    # message['Subject'] = 'title'

    #通过html修饰文本格式
    # with open('abc.html', 'r') as f:
    #     content = f.read()
    # html = MIMEText(content, 'html', 'utf-8')

    # with open('abc.txt', 'r')as h:
    #     content2 = h.read()
    # file = MIMEText(content2, 'plain', 'utf-8')
    # file['Content-Type'] = 'application/octet-stream'
    # file['Content-Disposition'] = 'attachment;filename="abc.txt"'


    #图片附件
    # with open('1.png', 'rb')as fp:
    #     picture = MIMEImage(fp.read())
    #     picture['Content-Type'] = 'application/octet-stream'
    #     picture['Content-Disposition'] = 'attachment;filename="1.png"'


    # 将内容附加到邮件主体中
    # message.attach(html)
    # message.attach(file)
    # message.attach(picture)



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

if __name__ == '__main__':
    main()
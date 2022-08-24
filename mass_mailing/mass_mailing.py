import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MassMailing:
    # 初始化邮件
    def __init__(self, send_to: list, title='无标题', mail_text='', *enclosure: str) -> None:
        '''
        send_to: 此参数为收件人列表可传入列表或元组类型数据
        title: 此参数为邮件标题
        mail_text: 此参数为邮件正文文字请传入字符串类型数据，建议为三引号的多行字符串
        enclosure: 此参数为邮件附件，传入数据为有效的文件路径组成的字符串,可传入多个字符串
        '''
        self.send_to = send_to
        self.title = title
        email_content = MIMEText(mail_text, 'plain', 'utf-8')  # 创建正文文本

        # 设置复合邮件对象
        self.msg = MIMEMultipart()
        self.msg.attach(email_content)  # 正文添加到复合邮件对象

        # 如果传入附件enclosure参数
        if len(enclosure) != 0:
            for file_path in enclosure:
                if '/' in file_path:
                    filename = file_path.split('/')[-1]
                else:
                    filename = file_path.split('\\')[-1]
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                attachment = MIMEText(file_data, 'base64', 'utf-8')  # 创建附件
                attachment.add_header(
                    'Content-Disposition', 'attachment', filename=filename)  # 附件添加标题
                self.msg.attach(attachment)  # 将附件添加到复合邮件对象

    # 设置账号信息
    def set_account(self, account, token, server_address, port):
        self.account = account
        self.token = token
        self.server_address = server_address
        self.port = port

    # 发送邮件
    def send_mail(self):
        smtp = smtplib.SMTP_SSL(self.server_address, self.port)
        smtp.login(self.account, self.token)  # 登录邮件服务器
        self.msg['From'] = self.account  # 发件人
        self.msg['Subject'] = self.title  # 邮件标题
        for mailto in self.send_to:
            self.msg['To'] = mailto  # 收件人
            try:
                smtp.sendmail(self.account, mailto,
                              self.msg.as_string())  # 发送邮件
                print(f'{mailto} 发送成功')
            except:
                print(f'{mailto} 发送失败')
        smtp.quit()  # 关闭邮箱服务
# =======================================上面的内容不建议修改=============================================
# 如果想在新的代码中引用此方法请将本文件放入新代码文件的同目录下然后写入以下语句：
# from mass_mailing import MassMailing  然后将【调试】部分代码写入新代码文件即可。

# 调试
if __name__ == '__main__':
    send_to = ['light22@126.com', 'ltmessager22@163.com',
               'light22@qq.com', 'light22@live.cn']  # 收件人列表

    title = '测试邮件'  # 邮件标题

    mail_text = '''
    你好：
        这是一封来自遥远星空彼岸的信件。
        你看到这封信一定很吃惊吧！
    '''  # 邮件正文

    fj1 = '附件1.txt'  # 邮件附件路径
    fj2 = r'D:\Codes\Python Projects\邮件群发\附件二.docx'  # 邮件附件路径
    fj3 = 'D:/Codes/Python Projects/邮件群发/第三个附件.xlsx'  # 邮件附件路径

    mail = MassMailing(send_to, title, mail_text, fj1, fj2, fj3)  # 实例化邮件

    account = 'light22@126.com'  # 你的邮箱账号
    token = 'XXXXXXXXXX'  # 你的邮箱授权码
    server_address = 'smtp.126.com'  # 你的邮箱smtp服务器地址
    port = 994  # 你的邮箱服务器端口号
    mail.set_account(account, token, server_address, port)  # 设置你的邮箱账号信息
    mail.send_mail()  # 发送邮件

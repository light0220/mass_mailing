from mass_mailing import MassMailing

send_to = ['light22@126.com', 'ltmessager22@163.com',
           'light22@qq.com', 'light22@live.cn']  # 收件人列表

title = '测试邮件'  # 邮件标题

mail_text = '''
你好：
    这是一封来自遥远星空彼岸的信件。
    你看到这封信一定很吃惊吧！
'''  # 邮件正文

fj1 = 'tests/附件1.txt'  # 邮件附件路径
fj2 = r'D:\Codes\Python Projects\邮件群发\tests\附件二.docx'  # 邮件附件路径
fj3 = 'D:/Codes/Python Projects/邮件群发/tests/第三个附件.xlsx'  # 邮件附件路径

mail = MassMailing(send_to, title, mail_text, fj1, fj2, fj3)  # 实例化邮件

account = 'light22@126.com'  # 你的邮箱账号
token = 'XXXXXXXXXXXXXXXX'  # 你的邮箱授权码
server_address = 'smtp.126.com'  # 你的邮箱smtp服务器地址
port = 994  # 你的邮箱服务器端口号
mail.set_account(account, token, server_address, port)  # 设置你的邮箱账号信息
mail.send_mail()  # 发送邮件

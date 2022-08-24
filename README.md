# 欢迎使用邮件群发

## 一、概述

本模块为方便大家更便捷使用Python来群发邮件而编写。

+ 作者：北极星光
+ E-mail：light22@126.com
+ Pypi官方库地址：https://pypi.org/project/mass-mailing-light22
+ Github地址：https://github.com/18513233125/mass_mailing

## 二、功能介绍

+ 简化复合邮件创建流程，省去繁长代码，只需要传入【收件人】、【邮件标题】、【正文文本】【附件路径】等信息即可一键创建复合邮件。
+ 无需导入繁复的库及函数，只需导入一个库即可一键发送邮件。
+ 一键群发邮件，无需担心各种报错导致程序中止，邮件发送完成后会提示哪些邮件发送成功，哪些发送失败，方便排查邮箱地址拼写等原因

## 三、使用方法

+ 模块下载方法：
  + 方法一：终端窗口输入命令 `pip install mass-mailing-light22`。
  + 方法二：去官方库地址 https://pypi.org/project/mass-mailing-light22 下载安装。
+ 导入本模块方法：
  + 在需要导入本模块的代码中写入导入语句：*`from excel_operate import ExcelOperate`。*
+ 对象实例化方法：
  + 通过语句 `mail = MassMailing(send_to, title, mail_text, fj1, fj2, fj3,...)`获得一个名为 `mail`的对象。
    + 参数 `send_to`*为收件人列表可传入由收件人地址字符串组成的列表或元组类型数据；*
    + *参数* `title`为邮件标题，可传入字符串类型数据，不传入数据则默认为【无标题】；
    + 参数 `mail_text`为邮件正文文本，可传入字符串类型数据，建议为三引号的多行字符串。也可不传入数据；
    + 参数 `fj1, fj2, fj3`为邮件附件，传入数据为有效的文件路径组成的字符串,可传入多个参数来添加多个附件，也可不传入此参数则无附件。
+ 设置发送邮箱账号信息：
  + 通过方法 `mail.set_account(account, token, server_address, port)`来设置发送邮箱的账号信息。
    + 参数 `account`为你的邮箱账号；
    + 参数 `token`为你的邮箱授权码；
    + 参数 `server_address`为你的邮箱smtp服务器地址；
    + 参数 `port`为你的邮箱服务器端口号。
+ 发送邮件：
  + 完成邮件对象实例化及发送邮箱账号信息参数设置这两步后即可发送邮件。
  + 发送邮件的代码为 `mail.send_mail()`。
+ 代码示例：
  ```
  from mass_mailing import MassMailing

  send_to = ['xxxx@126.com', 'xxxxx@163.com','xxxxxx@qq.com', 'xxxxxxx@live.cn']  # 收件人列表
  title = '邮件标题'  # 邮件标题
  mail_text = '''
  你好：
      这是一封来自遥远星空彼岸的信件。
      你看到这封信一定很吃惊吧！
  '''  # 邮件正文

  fj1 = 'tests/附件1.txt'  # 邮件附件路径
  fj2 = r'D:\Codes\Python Projects\邮件群发\tests\附件二.docx'  # 邮件附件路径
  fj3 = 'D:/Codes/Python Projects/邮件群发/tests/第三个附件.xlsx'  # 邮件附件路径

  mail = MassMailing(send_to, title, mail_text, fj1, fj2, fj3)  # 实例化邮件

  account = 'xxxxxxx@126.com'  # 你的邮箱账号
  token = 'XXXXXXXXXXXXXXXX'  # 你的邮箱授权码
  server_address = 'smtp.126.com'  # 你的邮箱smtp服务器地址
  port = 994  # 你的邮箱服务器端口号
  mail.set_account(account, token, server_address, port)  # 设置你的邮箱账号信息
  mail.send_mail()  # 发送邮件
  ```

## 四、版本历史

+ V 1.0.0
  + 初始版本

---

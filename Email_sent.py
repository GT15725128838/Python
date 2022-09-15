"""
yagmail 可以更简单的来实现⾃动发邮件功能。
(yagmail – Yet Another GMAIL/SMTP client)
"""
import yagmail

#链接邮箱服务器
# 1946326866@qq.com 发件⼈邮箱
# 12345 发件⼈邮箱授权码(授权码，注意不是邮箱密码)
# smtp.126.com ⽹易126邮箱发件服务器

yag = yagmail.SMTP( user="1946326866@qq.com", password="12345", host='smtp.126.com')

# 邮箱正⽂

contents = ['This is the body, and here is just text http://somedomain/image.png', 'You can find an audio file attached.', '/local/path/song.mp3']
# 发送邮件
# taaa@126.com 收件⼈邮箱
# subject 邮件主题
yag.send('taaa@126.com', 'subject', contents)
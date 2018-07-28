import smtplib
import email

host = 'smtp.googlemail.com'
port = 465
username = 'xxxxxxxxx@gmail.com'
password = 'xxxxxxxxxx'
sendto = ['email1' , 'email2']
body = 'my name is shivam'

con = smtplib.SMTP_SSL(host , port)
print(con.ehlo())
con.login(username , password)
con.sendmail(username , sendto , body)
con.quit()
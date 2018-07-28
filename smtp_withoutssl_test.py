import smtplib
import email

host = 'smtp.googlemail.com'
port = 587
username = 'xxxxxxxxxxx@gmail.com'
password = 'xxxxxxxxxxxxxx'
sendto = ['name@servername.com']
body = 'hi there'

con = smtplib.SMTP(host , port)
con.starttls()
print(con.ehlo())
con.login(username , password)
con.sendmail(username , sendto , body)
con.quit()

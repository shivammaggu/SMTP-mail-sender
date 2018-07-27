import smtplib
import email

host = 'smtp.googlemail.com'
port = 587
username = 'XXXXXXXXXXXXX@gmail.com'
password = 'XXXXXXXXXX'
sendto = ['name@servername.com']
body = 'hi there'

con = smtplib.SMTP(host , port)
con.starttls()
print(con.ehlo())
con.login(username , password)
con.sendmail(username , sendto , body)
con.quit()

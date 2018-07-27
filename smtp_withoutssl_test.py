import smtplib
import email

host = 'smtp.googlemail.com'
port = 587
username = 'shivammaggu1@gmail.com'
password = '2727SHIVAMmaggu2727'
sendto = ['shivammaggu1@gmail.com']
body = 'hi there'

con = smtplib.SMTP(host , port)
con.starttls()
print(con.ehlo())
con.login(username , password)
con.sendmail(username , sendto , body)
con.quit()

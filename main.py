from api_test import Login , Labels , cm , sm , Attach
class maybe:
	def main():
		sender = 'xxxxxxxxxxxxx@gmail.com'
		receiver = ['email1','email2','email3']
		subj = 'BETA TEST MAIL'
		bod = 'Dear all\nPlease reply \'positive\'                                                                    
		file = 'dit.png'
		l = Login.login()
		Labels.labels(l)
		for rec in receiver:
			#m = cm.create_message(sender,rec,subj,bod)
			#sm.send_message(l,'me',m)
			att = Attach.create_message_with_attachment(sender, rec, subj, bod, file)
			sm.send_message(l,'me',att)
maybe.main()

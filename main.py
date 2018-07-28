from api_test import Login , Labels , cm , sm , Attach
class maybe:
	def main():
		sender = 'shivammaggu1@gmail.com'
		receiver = ['Dheerajnegi794@gmail.com', 'pankujacks996@gmail.com', 'Tejeswichauhan888@gmail.com', 'vivek.semwal2@gmail.com', 'uditrawat106@gmail.com', 'vanshuhassija@gmail.com', 'parassengar38@gmail.com', 'ashishbhatt5380@gmail.com', 'namansworld1396@gmail.com', 'joshirricha@gmail.com', 'ayush.shukla1117@gmail.com', 'Mitalihanda.8@gmail.com', 'sraj02199@gmail.com', 'Him160895@gmail.com', 'Vaishalikhanduri55@gmail.com', 'goswami.siddh@gmail.com', 'Deveshgkp1@gmail.com', 'parassagarwal1279@gmail.com', 'rshvbhrdwj55@gmail.com', 'Tarunthakur108@gmail.com', 'Lsoni008@gmail.com', 'raghavag185918@gmail.com', 'Anujakapruwan16@gmail.com', 'tarunbhatt.cse@gmail.com', 'Shikhauniyal.uniyal0@gmail.com', 'vymsh95@gmail.com', 'goel.deepanshu888@gmail.com', 'smalik1197@gmail.com', 'shivammaggu1@gmail.com', 'Ashuworld242@gmail.com', 'rakshitmanhas@yahoo.com', 'mehrapooja985@gmail.com', 'gurleenkohli010@gmail.com', 'Korangaonduty3121@gmail.com', 'samyakjain1903@gmail.com', 'kb22880@gmail.com', 'mrinals597@gmail.com', 'pcghansiyal@gmail.com', 'divyakant3897@gmail.com', 'sonaliraijune@gmail.com', 'vipinshekhawat20@gmail.com', 'simrangoyal012@gmail.com', 'Soumyasrivastava189@gmail.com', 'pandeyvaishali2@gmail.com', 'Shbhmdvd@gmail.com', 'aashish10raj@gmail.com', 'pantsumit852@gmail.com', 'sugandhaagarwal2510@gmail.com', 'sakshamgoyal.sg@gmail.com', 'vermadeepak626@gmail.com', 'nikitabagwari123@gmail.com', 'arnav826awasthy@gmail.com', 'Rajat.shukla420@gmail.com', 'ankita.kumari455@gmail.com', 'ankiirawat24@gmail.com', 'sonalifotedar1996@gmail.com', 'samreenpopli96@gmail.com', 'rahul.ranjan2205@gmail.com', 'shantanusharmas011@gmail.com', 'Dydivyangi312@gmail.com', 'ayush.ankurgaur@gmail.com', 'phulerasanju20@gmail.com', 'divyagarwal77@gmail.com', 'rahultaneja03@gmail.com']
		#receiver = ['shivammaggu1@gmail.com' , 'shivammaggu1@gscditu.com']
		subj = 'BETA TEST MAIL'
		bod = 'Dear all\nPlease reply \'positive\' if you receive this mail.\nThis is necessary because I\'ll be sending all placement related information directly to your mail id.\nFrom now on please keep checking you emails and whatsapp group regularly to avoid missing any information.'                                                                    
		file = 'dit.png'
		l = Login.login()
		Labels.labels(l)
		for rec in receiver:
			#m = cm.create_message(sender,rec,subj,bod)
			#sm.send_message(l,'me',m)
			att = Attach.create_message_with_attachment(sender, rec, subj, bod, file)
			sm.send_message(l,'me',att)
maybe.main()

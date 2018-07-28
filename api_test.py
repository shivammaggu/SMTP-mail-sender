from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import argparse

class Login:
	def login():
		SCOPES = 'https://mail.google.com/'
		parser = argparse.ArgumentParser(parents=[tools.argparser])
		flags = parser.parse_args()
		store = file.Storage('credentials.json')
		creds = store.get()
		if not creds or creds.invalid:
		    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
		    creds = tools.run_flow(flow, store , flags)
		service = build('gmail', 'v1', http=creds.authorize(Http()))
		return service

class Labels:
	def labels(service):
		results = service.users().labels().list(userId='me').execute()
		labels = results.get('labels', [])
		if not labels:
		    print('No labels found.')
		else:
		    print('Labels:')
		    for label in labels:
		        print(label['name'])

import base64
from email.mime.text import MIMEText

class cm:
  def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

from googleapiclient.errors import HttpError

class sm:
  def send_message(service, user_id, message):
    try:
      print('sending email....')
      message = (service.users().messages().send(userId=user_id, body=message).execute())
      print('___email sent___')
      print('Message Id: %s' % message['id'])
      return message
    except HttpError as error:
      print('An error occurred: %s' % error)

from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import mimetypes
import os

class Attach:
  def create_message_with_attachment(sender, to, subject, message_text, file):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(message_text)
    message.attach(msg)
    content_type, encoding = mimetypes.guess_type(file)
    #print(content_type)
    #print(encoding)
    if content_type is None or encoding is not None:
      content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
      print('uploading text....')
      fp = open(file, 'rb')
      msg = MIMEText(fp.read(), _subtype=sub_type)
      fp.close()
    elif main_type == 'image':
      print('uploading image....')
      fp = open(file, 'rb')
      msg = MIMEImage(fp.read(), _subtype=sub_type)
      fp.close()
    elif main_type == 'audio':
      print('uploading audio....')
      fp = open(file, 'rb')
      msg = MIMEAudio(fp.read(), _subtype=sub_type)
      fp.close()
    elif main_type == 'application':
      print('uploading %s....' % sub_type)
      fp = open(file, 'rb')
      msg = MIMEApplication(fp.read(), _subtype=sub_type)
      fp.close()
    else:
      print('uploading %s (%s)....' % (main_type , sub_type) )
      fp = open(file, 'rb')
      msg = MIMEBase(main_type, sub_type)
      msg.set_payload(fp.read())
      fp.close()
    filename = os.path.basename(file)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

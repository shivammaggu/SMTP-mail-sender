from googleapiclient.errors import HttpError
class sm:
  def send_message(service, user_id, message):
    try:
      message = (service.users().messages().send(userId=user_id, body=message)
                 .execute())
      print('Message Id: %s' % message['id'])
      return message
    except HttpError as error:
      print('An error occurred: %s' % error)
      
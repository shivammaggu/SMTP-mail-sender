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
			        
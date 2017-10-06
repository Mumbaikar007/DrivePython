from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from apiclient.http import MediaFileUpload

#Set up a credentials object I think
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', ['https://www.googleapis.com/auth/drive'])

#Now build our api object, thing
drive_api = build('drive', 'v3', credentials=creds)

file_name = "test"
print ("Uploading file " + file_name + "...")

#We have to make a request hash to tell the google API what we're giving it
body = {'name': file_name, 'mimeType': 'application/vnd.google-apps.document'}

#Now create the media file upload object and tell it what file to upload,
#in this case 'test.html'
media = MediaFileUpload('test.html', mimetype = 'text/html')

#Now we're doing the actual post, creating a new file of the uploaded type
fiahl = drive_api.files().create(body=body, media_body=media).execute()

#Because verbosity is nice
print ("Created file '%s' id '%s'." % (fiahl.get('name'), fiahl.get('id')))



from httplib2 import Http
from oauth2client import file, client, tools
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from apiclient.http import MediaFileUpload

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)

drive_api = build('drive', 'v2', http=creds.authorize(Http()))	
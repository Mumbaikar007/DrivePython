from apiclient import errors
from apiclient.http import MediaFileUpload


file_metadata = {'name': 'photo.jpg'}
media = MediaFileUpload('banner-bg.jpg',
                        mimetype='image/jpeg')
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
print ('File ID: %s' % file.get('id'))

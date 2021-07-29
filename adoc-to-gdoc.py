#!/usr/bin/env python

from __future__ import print_function
import os.path
import sys
import subprocess
import getopt
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from apiclient.http import MediaFileUpload

def main(argv):

    SCOPES = ['https://www.googleapis.com/auth/drive']

    try:

        #pass filename as first argument
        filename = str(sys.argv[1])
        base_filename = os.path.splitext(filename)[0]
        upload_file = base_filename + ".docx"

        subprocess.call(["asciidoctor", "--backend", "docbook", "-a", "leveloffset=+1", "-a", "product-title='OpenShift Container Platform'", "-o", base_filename + ".xml", filename])
        subprocess.call(["pandoc", "-f", "docbook", "-t", "docx", "-s", base_filename + ".xml", "-o", base_filename + ".docx"])

        #Set up a credentials object
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        #Build the API object
        drive_api = build('drive', 'v3', credentials=creds)

        print ("Uploading file " + upload_file + "...")

        #Make a request hash to tell the google API what we're sending
        body = {'name': upload_file, 'mimeType': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}

        #Create the media file upload object and tell it what file to upload
        media = MediaFileUpload(os.path.abspath(upload_file), mimetype = 'text/html')

        #Now we're doing the actual post, creating a new file of the uploaded type
        file = drive_api.files().create(body=body, media_body=media).execute()

        print ("Created file '%s' id '%s'." % (file.get('name'), file.get('id')))
        print ("File is available at " + "https://docs.google.com/document/d/" + file.get('id'))

    except OSError as e:
        print(str(e))

    except getopt.GetoptError:
        #printUsage()
        sys.exit(2)

if __name__ == '__main__':
    main(sys.argv[1])
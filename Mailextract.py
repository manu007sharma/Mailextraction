import email
import os
import glob
import re
from email.parser import Parser  


path = 'C:\Downloader\PDF'
extension = 'eml'
os.chdir(path)

result = [i for i in glob.glob('*.{}'.format(extension))]

os.chdir('c:\Downloader\Invoice')         
count=0
for fle in result:  
      msg = email.message_from_file(open(os.path.join(path,fle)))
      to=msg['To']
      fromm=msg['from']
      if "word" in to: # to filter any irrelevent mails
          attachments=msg.get_payload()
          for attachment in attachments:
              try:
                  fnam=attachment.get_filename().lower()
                  if "initial" in fnam:   AGain filtering any irreleveant attachement
                      fr=msg['subject'].split()
                      dname=fr[6]+'.pdf'
                      f=open(dname, 'wb').write(attachment.get_payload(decode=True,))
                      count=count+1
                      f.close()
                  else:
                      pass
              except Exception as detail:
                  pass  

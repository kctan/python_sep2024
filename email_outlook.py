# need to install the pywin32 library
# pip install pywin32

import win32com.client

subject = 'email subject'
body = '<html><body>' + 'testing' + '</body></html>'
recipient = '<SOME EMAIL>'
#attachments = ["D:\\abc.txt"]

#Create and send email
olMailItem = 0x0
obj = win32com.client.Dispatch("Outlook.Application")
newMail = obj.CreateItem(olMailItem)
newMail.Subject = subject
newMail.HTMLBody = body
#newMail.Body = body
newMail.To = recipient

#for location in attachments:
#    newMail.Attachments.Add(Source=location)

#newMail.display()
newMail.Send()

#pip install pywin32

import win32com.client

#Create and send appointment
outlook = win32com.client.Dispatch("Outlook.Application")
appt = outlook.CreateItem(1) # AppointmentItem, 0 - Email
appt.Start = "2021-11-05 17:35" # yyyy-MM-dd hh:mm
appt.Subject = "Subject of the meeting"
appt.Duration = 60 # In minutes (60 Minutes)
appt.Location = "Location Name"

# 1 - olMeeting; Changing the appointment to meeting.
# Only after changing the meeting status recipients can be added
appt.MeetingStatus = 1
  
appt.Recipients.Add("abc@rp.edu.sg") # Don't end ; as delimiter

appt.Save()
appt.Send()
print("Sent")
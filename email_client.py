#Author:S M Abdullah Ferdous as a Part of CM2540 final coursework
#this is the class to send a email to the Admin once the motion is detected
import smtplib
import email.utils
from email.message import Message
import getpass
import datetime

class email_client:
    def __init__(self):
        # initialise email credentials from file
        with open('email_credentials.txt', 'r') as data_file:
            lines = data_file.readlines()
        to_email = lines[0].strip()
        self.servername = lines[1].strip()
        self.username = lines[2].strip()
        self.password = lines[3].strip()
        from_sender_name = lines[4].strip()
        from_sender_email = lines[5].strip()

        # Create the message
        self.msg = Message()
        self.msg['To'] = email.utils.formataddr(('Recipient', to_email))
        self.msg['From'] = email.utils.formataddr((from_sender_name, from_sender_email))

        self.msg['Date'] = email.utils.formatdate(localtime = 1)
        self.msg['Message-ID'] = email.utils.make_msgid()
    #method to send the email
    def send_email(self, subject, body):
        self.msg['Subject'] = subject
        self.msg.set_payload(body)
        self.server = smtplib.SMTP(self.servername)
        try:
            # for verbose reporting
            self.server.set_debuglevel(True)

            # identify ourselves, prompting server for supported features
            self.server.ehlo_or_helo_if_needed()

            # If we can encrypt this session, do it
            if self.server.has_extn('STARTTLS'):
                self.server.starttls()
                # re-identify ourselves over TLS connection
                self.server.ehlo_or_helo_if_needed() 

            self.server.login(self.username, self.password)
            
            self.server.send_message(self.msg)
        finally:
            self.server.quit()
#testing the method
if __name__ == '__main__':
    emailer = email_client()
    body = ('intruder detected at {}'.format(datetime.datetime.now()))
    emailer.send_email('intruder detected', body)

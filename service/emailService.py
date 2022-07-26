from dotenv import load_dotenv
import smtplib
import os
from email.message import EmailMessage
load_dotenv()

'''
This module is going to send emails to the client and agent.

Client: list of top 5 matches and contact info.
Agent: Client name, their matches, email.

That is really it. Not much to this here. 

I don't LOVE the use of BaseException here, but I mean...
we got an app to develop.

But I will admit this it technical debt.
'''


def send_to_agent():
    try:
        msg = EmailMessage()
        msg.set_content("SENT FROM ZENITH LOCATORS API.")
        msg['Subject'] = 'Allow Me To Introduce Myself.'
        msg['From'] = os.environ.get("EMAIL_USER")
        msg['To'] = 'james.garcia1201@outlook.com'
        mail_server = smtplib.SMTP(os.environ.get("EMAIL_SERVER"), 587)
        mail_server.starttls()
        mail_server.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
        print("logged in successfully")
        mail_server.send_message(msg)
        mail_server.quit()
        return True
    except BaseException as error:
        return False

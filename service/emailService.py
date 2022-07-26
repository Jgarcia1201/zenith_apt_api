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

But I will admit this is technical debt.

!!!!!!!!!!!!!!!!!!!!REMEMBER TO CHANGE THE RECIPIENT EMAIL IN SEND_TO_AGENT!!!!!!!!!!!!!!!!!!!!!!!!!!!!

'''


def send_to_agent(client):
    try:
        msg = EmailMessage()
        msg['Subject'] = 'NEW LEAD: {}'.format(client['name'])
        msg['From'] = os.environ.get("EMAIL_USER")
        msg['To'] = 'james.garcia1201@outlook.com'
        mail_server = smtplib.SMTP(os.environ.get("EMAIL_SERVER"), 587)
        mail_server.starttls()
        mail_server.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
        client_matches_info = get_match_info(client["matches"])
        msg.set_content("""\
            <html>
            <head></head>
            <body>
                <h3>We Got a New Lead!</h3>
                <h5>Name: {}</h3>
                <h5>Email: {}</h3>
                <h5>Here are the apartments we sent over:</h5>
                {}
            </body>
            </html>
        """.format(client["name"], client["email"], "<br/>".join(client_matches_info)), subtype='html')
        mail_server.send_message(msg)
        mail_server.quit()
        return True
    except BaseException as error:
        return False


def get_match_info(arr):
    to_return = []
    for apt in arr:
        temp = "Name: {} | Phone: {}".format(apt["name"], apt["phone"])
        to_return.append(temp)
    return to_return


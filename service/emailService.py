from dotenv import load_dotenv
import smtplib
import os
from email.message import EmailMessage

load_dotenv()

'''
This module sends emails to the client and agent.

Client: list of top 5 matches and contact info.
Agent: Client name, their matches, email.

I don't LOVE the use of BaseException here, but I mean...
we got an app to develop.

But I will admit this is technical debt.

!!!!!!!!!!!!!!!!!!!!REMEMBER TO CHANGE THE RECIPIENT EMAIL IN SEND_TO_AGENT!!!!!!!!!!!!!!!!!!!!!!!!!!!!

In future versions, I could probably decorate the email with CSS using <style> tags and {}
then using a string to hold the CSS and .format to insert it in between the style tags.

'''


def send_to_agent(client):
    try:
        msg = EmailMessage()
        msg['Subject'] = 'NEW LEAD: {}'.format(client['name'])
        msg['From'] = os.environ.get("EMAIL_USER")
        msg['To'] = client["email"]
        mail_server = smtplib.SMTP(os.environ.get("EMAIL_SERVER"), 587)
        mail_server.starttls()
        mail_server.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
        client_matches_info = get_match_info_agent(client["matches"])
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


def get_match_info_agent(arr):
    to_return = []
    for apt in arr:
        temp = "Name: {} | Phone: {}".format(apt["name"], apt["phone"])
        to_return.append(temp)
    return to_return


def send_to_client(client):
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Your Matches From Zenith Locators'
        msg['From'] = os.environ.get("EMAIL_USER")
        msg['To'] = client["email"]
        mail_server = smtplib.SMTP(os.environ.get("EMAIL_SERVER"), 587)
        mail_server.starttls()
        mail_server.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
        client_matches_info = get_match_info_client(client["matches"])
        msg.set_content("""\
            <html>
            <head></head>
            <body>
                <h4>Hello, {}</h4>
                <h5>Thank You For Choosing Zenith Locators.</h5>
                <h5>We analyzed your profile and found some apartments we think you'll love.</h3>
                <h5>If you're interested in any of these apartments, simply respond to this email or give us a call at:
                    <br/><br> 
                    Phone: {}
                </h5>
                <h5>Here are your {} personalized matches:</h5>
                {}
                <p>We once again thank you for choosing Zenith and we look forward to hearing from you.</p>
            </body>
            </html>
        """.format(client["name"], os.environ.get("PHONE"), len(client_matches_info), "<br/><br/>".join(client_matches_info)), subtype='html')
        mail_server.send_message(msg)
        mail_server.quit()
        return True
    except BaseException as error:
        return False


def get_match_info_client(arr):
    to_return = []
    for apt in arr:
        temp = "<h4>{}. {}</h4><img src={}></img>".format(arr.index(apt)+1, apt["headline"], apt["img"])
        to_return.append(temp)
    return to_return


def send_no_matches(client):
    try:
        msg = EmailMessage()
        msg['Subject'] = 'A Message From Zenith Locators'
        msg['From'] = os.environ.get("EMAIL_USER")
        msg['To'] = client["email"]
        mail_server = smtplib.SMTP(os.environ.get("EMAIL_SERVER"), 587)
        mail_server.starttls()
        mail_server.login(os.environ.get("EMAIL_USER"), os.environ.get("EMAIL_PASS"))
        msg.set_content("""\
            <html>
            <head></head>
            <body>
                <h4>Hello, {}</h4>
                <h5>Thank You For Choosing Zenith Locators.</h5>
                <h5>
                    We analyzed your profile and couldn't find any matches in our database.
                    We would still love to help you find a new apartment! 
                </h5>
                <h5>
                    Simply respond to this email or contact us at:
                    <br/>
                    Phone {}
                </h5>
                <p>We once again thank you for choosing Zenith and we look forward to hearing from you.</p>
            </body>
            </html>
        """.format(client["name"], os.environ.get("PHONE")), subtype='html')
        mail_server.send_message(msg)
        mail_server.quit()
        return True
    except BaseException as error:
        return False

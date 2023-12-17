#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText

def sendmail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'sandbox.smtp.mailtrap.io'
    login = '9f706ed1e538b5'
    password = 'afa9e4477b3adf'
    message = f"""<h3>New Feedback</h3><ul><li>Customer: {customer}</
    li><li>Dealer: {dealer}</li><li>Rating: {rating}</
    li><li>Comments: {comments}</li></ul>"""
    
    sender = 'email1@example.com'
    receiver = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender
    msg['To'] = receiver
    
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender, receiver, msg.as_string())
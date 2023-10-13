from email.message import EmailMessage
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

path = "TicketStatus/functions/credentials.json"

with open(path, 'r') as json_file:
    data = json.load(json_file)

email_sender = data["email_sender"]
email_password = data["email_password"]

def send_email(data):
    emailData =f'''
    <!DOCTYPE html>
    <html>
    <body style="padding:4px; background-color: #000; color: #FFF; font-family: Arial, sans-serif;">
        <h2 style="color: #9bff00;">Dear {data['nameOfPassenger']},</h2>
        <p>Your booking status for Train No. {data['TrainNo']} - {data['TrainName']} from {data['From']} to {data['To']} is as follows:</p>
        <table style="width: 100%; max-width: 800px; margin: 20px auto;">
            <tr>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">Prediction Percentage:</td>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">{data['PredictionPercentage']}</td>
            </tr>
            <tr>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">Prediction:</td>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">{data['Prediction']}</td>
            </tr>
            <tr>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">Date of Journey:</td>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">{data['DateOfJourney']}</td>
            </tr>
            <tr>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">Class:</td>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">{data['Class']}</td>
            </tr>
            <tr>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">Coach:</td>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">{data['Coach']}</td>
            </tr>
            <tr>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">Berth:</td>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">{data['Berth']}</td>
            </tr>
            <tr>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">Coach Position:</td>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">{data['CoachPosition']}</td>
            </tr>
            <tr>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">Booking Status:</td>
                <td style="border: 1px solid #666; padding: 10px; text-align: left;">{data['BookingStatus']}</td>
            </tr>
        </table>
    </body>
    </html>
    '''

    email_reciever =data['passengerEmail']
    subject = f"Ticket Status for {data['TrainNo']} {data['TrainName']}"

    em = MIMEMultipart()
    em['From'] = email_sender
    em['To']= email_reciever
    em['subject'] = subject
    em.attach(MIMEText(emailData, "html"))
    em.as_string()
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

    return {
        "success":True,
        "message":"Email sent successfully."
        }
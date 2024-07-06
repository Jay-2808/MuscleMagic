import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import formataddr
from email import encoders
from email.mime.image import MIMEImage
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')

#Subject and Body of the mail
subject = 'Fee Reminder'
text = 'This is a reminder to pay your fee.'

def send_fee_reminder(to, User_Id,User_Name,Current_Plan,Current_Plan_amount,Status,Due_Date,CEO_Name,Contact, image_path=None, attachment_path=None):
    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = formataddr(("Muscle Magic Fitness Studio",f"{EMAIL_USER}"))
    msg['To'] = to

    # Create the body with both plain text and HTML parts
    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)

    # Plain text part
    msg_text = MIMEText(text, 'plain')
    msg_alternative.attach(msg_text)

    # HTML part
    html_content = f"""
    <html>
        <body>
            <p>Dear {User_Name},</p>
            <p>We hope this message finds you well. This is a friendly reminder from Muscle Magic Unisex Fitness Studio to inform you that <strong>your membership fee is due soon.</strong>
            Your User ID is {User_Id}, and you are currently subscribed to the {Current_Plan} plan. The amount due for this plan is <strong>&#x20B9;{Current_Plan_amount}</strong>
            
            <p>Also please ensure to make the payment by the due date <strong>{Due_Date}.</strong>and continue enjoying our services.</P>

            <p>We greatly value your membership and commitment to fitness with us. Should you have any questions or need assistance regarding your membership or payment, 
            please do not hesitate to reach out to us at {Contact}.</p>

            <p>Your membership details are as follows:
                <br>User ID: {User_Id}
                <br>Current Plan: {Current_Plan}
                <br>Amount Due: &#x20B9;{Current_Plan_amount}
                <br>Due Date: {Due_Date}
            </p>

            <p>Also, feel free to explore our other membership plans for options that may better suit your fitness goals.</p><br>
    """
    if image_path:
        cid = os.path.basename(image_path)
        html_content += f'<img src="cid:{cid}">'
    html_content += f"""
            <p>Thank you for choosing <strong>Muscle Magic Unisex Fitness Studio.</strong></P>

            <p>Best regards,
            <br>{CEO_Name}
            <br><a href="www.musclemagic.in">www.musclemagic.in</a>
            <h3 style="color:red">Muscle Magic Unisex Fitness Studio<br>{Contact}</h3>
        </body>
    </html>
    """
    msg_html = MIMEText(html_content, 'html')
    msg_alternative.attach(msg_html)

    if image_path:
        try:
            with open(image_path, 'rb') as img:
                img_data = img.read()
                image = MIMEImage(img_data, name=os.path.basename(image_path))
                image.add_header('Content-ID', f'<{cid}>')
                image.add_header('Content-Disposition', 'inline', filename=os.path.basename(image_path))
                msg.attach(image)

            print(f"Embedded image: {image_path}")
        except Exception as e:
            print(f"Error embedding image: {e}")

    if attachment_path:
        try:
            with open(attachment_path, 'rb') as attach_file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attach_file.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(attachment_path)}'
                )
                msg.attach(part)
                
            print(f"Attached file: {attachment_path}")
        except Exception as e:
            print(f"Error attaching file: {e}")

    try:
        with smtplib.SMTP('smtp.office365.com', 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, to, msg.as_string())
        print(f"Sent email to {to}")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

    return "Email sent successfully",200
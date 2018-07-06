import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
QRFILES_FOLDER = os.path.join(PROJECT_ROOT, 'tickets/')


def send_email(to, uuid, name, reg_no, mobile_no, event_name):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Ticket Details'
    msgRoot['From'] = 'anmolchawla10@gmail.com'

    # Create the body of the message.
    html = """\
        <p align="center"><b>AARUUSH'18</b></p>
        <p align="center"><b>CONFIRMATION RECIEPT</b></p>
        <p align="left"><b>Name</b> : """ + str(name) + """</p>
        <p align="left"><b>Register Number</b> : """ + str(reg_no) + """</p>
        <p align="left"><b>Mobile Number</b> : """ + str(mobile_no) + """</p>
        <p align="left"><b>Event Name</b> : """ + str(event_name) + """</p>
        <p>
            <img src="cid:image1">
        </p>
    """

    # Record the MIME types.
    msgHtml = MIMEText(html, 'html')
    img = open(QRFILES_FOLDER + 'QRCodes/' + uuid + '.png', 'rb').read()

    msgImg = MIMEImage(img, 'png')
    msgImg.add_header('Content-ID', '<image1>')
    msgImg.add_header('Content-Disposition', 'inline',
                      filename=QRFILES_FOLDER + 'QRCodes/' + uuid + '.png')

    msgRoot.attach(msgHtml)
    msgRoot.attach(msgImg)
    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    recipients = [to]
    recipients.append('anmolchawla10@outlook.com')
    smtp.login('anmolchawla10@gmail.com', '@nm0lp42cdel')
    smtp.sendmail('anmolchawla10@gmail.com', recipients, msgRoot.as_string())
    smtp.quit()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
QRFILES_FOLDER = os.path.join(PROJECT_ROOT, 'tickets/')


def send_email(to, uuid):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Ticket Details'
    msgRoot['From'] = 'anmolchawla10@gmail.com'

    # Create the body of the message.
    html = """\
        <p>Hello,</p>
        <p> Attached below is the qr code for the ticket </p>
        <p>
            <img src="cid:image1">
        </p>
    """

    # Record the MIME types.
    msgHtml = MIMEText(html, 'html')
    img = open(QRFILES_FOLDER + 'QRCodes/' + uuid +'.png', 'rb').read()

    msgImg = MIMEImage(img, 'png')
    msgImg.add_header('Content-ID', '<image1>')
    msgImg.add_header('Content-Disposition', 'inline', filename=QRFILES_FOLDER + 'QRCodes/' + uuid +'.png')

    msgRoot.attach(msgHtml)
    msgRoot.attach(msgImg)
    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()
    smtp.login('anmolchawla10@gmail.com', '@nm0lp42cdel')
    smtp.sendmail('anmolchawla10@gmail.com', to, msgRoot.as_string())
    smtp.quit()

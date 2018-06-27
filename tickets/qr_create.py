import pyqrcode
import os

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
QRFILES_FOLDER = os.path.join(PROJECT_ROOT, 'tickets/')

def create_qrcode(uuid):
    qr = pyqrcode.create(uuid)
    qr.png ((QRFILES_FOLDER + 'QRCodes/' + uuid +'.png'), scale=6)

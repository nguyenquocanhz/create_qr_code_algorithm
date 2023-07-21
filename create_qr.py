import qrcode
from PIL import Image
import random

def create_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="blue", back_color="white")

    # Save the QR code image with a random filename
    file_path = f'qr_code{random.randint(1000, 9999)}.png'
    qr_image.save(file_path)

    return file_path

if __name__ == "__main__":
    qr_data = "0397426841"
    qr_image_path = create_qr_code(qr_data)
    print(f"QR Code has been created and saved as: {qr_image_path}")

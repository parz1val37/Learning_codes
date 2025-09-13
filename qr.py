import qrcode
from qrcode.constants import ERROR_CORRECT_H


data = "FUCK YOU🖕🏿! BITCH"


qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
print("QR code saved as qrcode.png")


print("\nSCAN ON YOUR OWN RISK:\n")
qr.print_ascii(invert=True)   
import qrcode

data = input("Enter test of URL: ").strip()
filename = input("Enter the file name: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{filename}.png")
print(f"QR code saved as {filename}.png")
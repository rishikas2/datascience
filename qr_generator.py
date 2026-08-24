import qrcode

data=input("Enter the text or URL: ").strip()
filename= input("enter filename: ").strip()
qr= qrcode.QRCode(box_size=10, border=5)
qr.add_data(data)
image=qr.make_image(fill_color="black", back_color="white")
image.save(f"{filename}.png")
print(f"QR code saved as {filename}.png")
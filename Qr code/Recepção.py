import qrcode

# caminho da imagem (muito pequena, tipo 50x50)
data = open("imagem_pequena.png", "rb").read()

qr = qrcode.QRCode(version=10, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("qrcode_com_imagem.png")
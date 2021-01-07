import qrcode
qr=qrcode.QRCode(version=1,box_size=15,border=5)
data=input("Enter the data you want to be inserted in the qrcode : ")
qr.add_data(data)
img=qr.make_image()
img.save("qrcode.jpg")                                   #if the prefered image formate is jpg
#img.save("qrcode.png")                                   #if the prefered image formate is png

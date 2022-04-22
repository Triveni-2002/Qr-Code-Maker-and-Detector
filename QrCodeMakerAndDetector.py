import qrcode
import cv2
s=input()
img=qrcode.make(s)
img.show()
img.save("yoda.jpg")
d=cv2.QRCodeDetector()
val,points,s=d.detectAndDecode(cv2.imread("yoda.jpg"))
print("Decoding value for a given string from Qrcode:",val)

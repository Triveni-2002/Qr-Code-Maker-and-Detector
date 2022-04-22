import qrcode
import cv2
img=qrcode.make("www.google.com")
img.show()
img.save("yoda.jpg")
d=cv2.QRCodeDetector()
val,points,s=d.detectAndDecode(cv2.imread("yoda.jpg"))
print(val)

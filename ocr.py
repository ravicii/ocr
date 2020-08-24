import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
vid=cv2.VideoCapture(0)
def ocr(img):
    boxes=pytesseract.image_to_data(img)
    for c,box in enumerate(boxes.splitlines()):
        if c!=0:
            box=box.split()
            if len(box)==12:
                x,y,w,h,text=int(box[6]),int(box[7]),int(box[8]),int(box[9]),box[-1]
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(img,text,(x,y+h+20),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)
    return img
#to load from the webcam, live

while True:
    ret,img=vid.read()
    cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=ocr(img)
    cv2.imshow('Result',img)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        cv2.destroyAllWindows()
        break
#to load an image from your drive
'''
img=cv2.cvtColor(cv2.imread('test-ocr.png'),cv2.COLOR_BGR2RGB)
img=ocr(img)
cv2.imshow('Result',img)
cv2.waitKey(0)
'''
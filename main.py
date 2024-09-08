import easyocr
import cv2
reader = easyocr.Reader(['ar', 'en'])  # this needs to run only once to load the model into memory

img = cv2.imread('input/19.jpg')

result = reader.readtext(img, detail=0, paragraph=True)

print(result)

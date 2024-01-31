from PIL import Image
import pytesseract
import cv2  # if we want to recognize spreadsheet image, we need to install it by 'pip install opencv-python'



aimImG = 'C:\\Users\\f.he\\OneDrive - AuCom Group\\Desktop\\tesseractTEST\\table3.png'

raw = cv2.imread(aimImG, 1)

gray = cv2.cvtColor(raw, cv2.COLOR_BAYER_BG2BGR)

binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,35,-5)

cv2.imshow("binary_picture", binary)


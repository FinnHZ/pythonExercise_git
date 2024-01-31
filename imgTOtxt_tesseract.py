from PIL import Image
import pytesseract
import cv2  # if we want to recognize spreadsheet image, we need to install it by 'pip install opencv-python'

aimImG = 'C:\\Users\\f.he\\OneDrive - AuCom Group\\Desktop\\tesseractTEST\\testNonStandard.png'



pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\f.he\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"



print( 
    #  type(
    pytesseract.image_to_string(
    Image.open(
    aimImG
    )
    )
    # )
     )
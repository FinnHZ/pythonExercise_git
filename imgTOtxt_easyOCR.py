
#pip install torch torchvision torchaudio
#pip install easyocr


"""This method must be used based on network connection."""

import easyocr  



aimImG = 'C:\\Users\\f.he\\OneDrive - AuCom Group\\Desktop\\tesseractTEST\\table3.png'




reader = easyocr.Reader(['en'])
result = reader.readtext(aimImG, detail = 0)
print(result)
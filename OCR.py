#MANU
#manupoonia78@gmail.com

import os
import cv2
import pytesseract
import re
import json

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
directory = "D:\\"

image = cv2.imread((os.path.join(directory,"SAMPLE.jpg")))

#thresholding the image to reduce noise
ret,thresh = cv2.threshold(image,115,255,cv2.THRESH_BINARY)

#Extracting texts in the form of strings
text = pytesseract.image_to_string(thresh,lang='eng')

license_ocr={}
splits = text.splitlines()

#Finding lines that contain 'Name'
for i in range(0,len(splits)):
  if re.search(r'Name',splits[i]):
    break;

#Removing 'Name' from the obtained string
name1=splits[i][5:len(splits[i])-3]
name=name1+' '+splits[i+1]
license_ocr['Name']=name

#Finding lines that contain 'Address'
for i in range(0,len(splits)):
  if re.search(r'Ad[a-z]*ss',splits[i]):
    break;
  
#Removing 'Address' from the obtained string
address1=splits[i][9:]
address=address1+''+splits[i+1]+' '+splits[i+2]
license_ocr['Address']=address

#Finding 'BG' in (i+3)th line
BG_pattern=r'([B][G]\s[A-Z])'
blood_group = re.search(BG_pattern,splits[i+3]).group()

#Removing 'BG' from the obtained string
bg=blood_group[len(blood_group)-1]
license_ocr['Blood Group']=bg

#Finding Telephone Number in (i+4)th line
phone_pattern=r'([0-9]{10})'
phone_number = re.search(phone_pattern,splits[i+4]).group()
license_ocr['Phone Number']=phone_number

#Finding License ID in (i+5)th line
license_id_pattern=r'([A-Z]{2}\s[\w]{6}\s[A-Z]{2}\s[A-Z]{2})'
license_id = re.search(license_id_pattern,splits[i+5]).group()
license_ocr['License ID']=license_id

#Finding DOB in the whole text
date_pattern = r'(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/](19|20)\d\d'
date = re.search(date_pattern,text).group()
license_ocr['DOB'] = date

#Converting Python Dictionary to a Json File
license_json = json.dumps(license_ocr)

#Printing the JSON File
print(license_json)

cv2.waitKey(0)





MANU
manupoonia78@gmail.com

1. PREPROCESSING OF THE IMAGE
Before begining extraction, 
since most of the image contains different noises to remove those noises so that i can clearly extract the texts, i did 
thresholding of the image provided by cv2 libraby 

2. TEXT EXTRACTION
Using the pytesseract module and img_to_string() methods recognizable texts are extracted from the image
image_to_string() methods can take many languages, so i provided english in which the text format is given

3. INFORMATION SEARCHING
I used regular expression module and its methods to find the desired information from the extracted text and 
store that in the a python dictionary

4. DATA CONVERSION
At last I converted that python dictonary to a JSON File 
and printed it
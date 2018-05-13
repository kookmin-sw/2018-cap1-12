#import Image
import sys
from PIL import Image
import pytesseract

im = Image.open(sys.argv[1])
print im
im.show()
text = pytesseract.image_to_string(im, lang='kor')
print text
#print pytesseract.image_to_string(Image.open(sys.argv[1]))


#python qrcode.py d:\Users\admin\Desktop\exces.txt d:\Users\admin\Desktop\qwerr .png 50 50 

# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
import sys
import os
from PIL import Image

with open(sys.argv[1], 'r') as f:
    contents = f.read()

      
# Generate QR code 
url = pyqrcode.create(contents) 

fn = sys.argv[2]
type = sys.argv[3]
w = int(sys.argv[4])
h = int(sys.argv[5])

# Create and save the png file naming "myqr.png" 
y = ".png"
url.png(sys.argv[1] + y, scale = 6)
img = Image.open(sys.argv[1] + y)
img1 = img.resize((w,h))
img1.save(sys.argv[2] + type)  
os.remove(sys.argv[1] + y)

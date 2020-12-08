# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
import sys
from PIL import Image
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

label1 = tk.Label(root, text='CONVERT TO QRCODE')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter file name')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

label3 = tk.Label(root, text='NOTE: Enter the path of txt file example-' )
label3.config(font=('helvetica', 8))
canvas1.create_window(200, 235, window=label3)

label4 = tk.Label(root, text=r'd:\Users\admin\Desktop\filename' )
label4.config(font=('helvetica', 8))
canvas1.create_window(200, 253, window=label4)


entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getqr ():  
    x1 = entry1.get()
    x2 = ".txt"

    f = open(x1 + x2, "r")
    contents = f.read()

    # Generate QR code 
    url = pyqrcode.create(contents) 
  
    # Create and save the png file naming "myqr.png" 
    y = ".png"
    url.png(x1 + y, scale = 6)
    
    im = Image.open(x1 + y)
    im.show()
    
    
button1 = tk.Button(text='Get QRCODE', command=getqr, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()


    
      


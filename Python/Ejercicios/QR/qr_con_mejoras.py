import qrcode                                                       


link = str(input("¿Cuál es el link del que quieres crear el QR? "))

ver = int(input("¿Qué tan complejo quieres el QR (1-5): "))
size = int(input("¿Qué tan grande quieres el QR (5-10): "))
bor = int(input("¿Qué tan grueso quieres el borde QR (1-5): "))

qr = qrcode.QRCode(version = ver, box_size = size, border = bor)          
qr.add_data(link)                                           
qr.make()                                                          

fcolor = str(input("¿De que color quieres el fondo del QR? "))
qrcolor = str(input("¿De que color quieres el QR? "))

img = qr.make_image(fill_color = fcolor, back_color = qrcolor)    
img.save('helen.png')                                        

"""
To improve this, we could do a couple of things:

- Done - Allow the website link to be typed in using input() function.
- Done -  Allow users to customize the QR code generated.
- Automate the process to create multiple QR codes.
- Include more functions (or object parameters) of the qrcode library.
- Try changing the colors and styles of the generated QR codes using different drawer modules and fill colors.
- Use an application library (like Tkinter) to add a user interface.
- Check out other QR code libraries like pyqrcode.
"""

import qrcode                                                       # importa la librería para poder hacer el QR

website_link = 'https://www.youtube.com/'               # Ponemos la url a abrir con el qr

qr = qrcode.QRCode(version = 3, box_size = 10, border = 5)          # Cambia los atributos, version es que "tan complejo será", bozsize "tamaño del qr", border es el borde "fuera del qr"    
qr.add_data(website_link)                                         # toma la info del website link para crear el qr
qr.make()                                                           # Crea el qr

img = qr.make_image(fill_color = 'white', back_color = 'black')     # Ponemos los colores a usar
img.save('llamada.png')                                           # Como se guarda la imagen y donde



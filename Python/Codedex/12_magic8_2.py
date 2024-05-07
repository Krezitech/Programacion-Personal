# Bola mágica
import random

pregunta = input("Has tu pregunta: ")
numero = random.randint(1, 9)

if numero == 1:
    respuesta = "Si, Definitivamente"
elif numero == 2:
    respuesta = "Parece ser que si"
elif numero == 3:
    respuesta = "sin duda"
elif numero == 4:
    respuesta = "No lo veo claro, pregunta de nuevo"
elif numero == 5:
    respuesta = "Pregunta mas tarde"
elif numero == 6:
    respuesta = "Mejor no te digo"
elif numero == 7:
    respuesta = "Mis fuentes dicen que no"
elif numero == 8:
    respuesta = "Las probabilidades no son buenas"
elif numero == 9:
    respuesta = "No lo creo Rick..."
else:
    respuesta = "Hubo algún error"

print("Pregunta: ", pregunta)
print("Respuesta: ",respuesta)
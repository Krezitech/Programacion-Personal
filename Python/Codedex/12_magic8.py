# Bola mágica
import random

uno = "Si, Definitivamente"
dos = "Parece ser que si"
tres = "sin duda"
cuatro = "No lo veo claro, pregunta de nuevo"
cinco = "Pregunta mas tarde"
seis = "Mejor no te digo"
siete = "Mis fuentes dicen que no"
ocho = "Las probabilidades no son buenas"
nueve = "No lo creo Rick..."


pregunta = input("Has tu pregunta: ")

respuesta = random.randint(1, 9)

if respuesta == 1:
    print(uno)
elif respuesta == 2:
    print(dos)
elif respuesta == 3:
    print(tres)
elif respuesta == 4:
    print(cuatro)
elif respuesta == 5:
    print(cinco)
elif respuesta == 6:
    print(seis)
elif respuesta == 7:
    print(siete)
elif respuesta == 8:
    print(ocho)
elif respuesta == 9:
    print(nueve)
else:
    print("Hubo algún error")
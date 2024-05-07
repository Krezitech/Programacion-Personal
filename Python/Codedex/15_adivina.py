
adivina = 0
intentos = 3

print("Para ganar tienes que adivinar el número secreto")
print("Sólamente tienes 3 intentos")

while adivina !=6 and intentos > 0:
    adivina = int(input("Vuelve a intentar adivinar el número secreto: "))
    intentos = intentos - 1
    print("Te quedan ",intentos, " intentos")
    
if intentos == 0:
    print("Perdiste")
    

if adivina == 6:
    print("Ganaste!!!")
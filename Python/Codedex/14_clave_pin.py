# Creando un acceso de password

print("Bienvenido a tu Banco")
pin = int(input("Por favor inserta tu numero secreto para acceder "))

""""
if pin == 210526:
    print ("Bievenido a tu sesión")
else:
    print("Tu pin es inválido")

# Esto haría que solo funcionase una sola vez para ver si accede o no

"""

while pin != 210526:                                    # Entra en el loop hasta q se cumpla la condición
    print("Tu pin es inválido")
    pin = int(input("Por favor vuelve a intentar "))    # Se reinsertta la nueva condición para volver a intentar

if pin == 210526:
    print("Bienvenido a tu sesión") 
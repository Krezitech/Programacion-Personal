# Condicionales

my_condition = True 

if my_condition:
    print("Se ejecuta la condición del IF")

print("la ejecución continua")

my_condition = False

if my_condition:
    print("Esta NO SE EJECUTA")

print("Esta si, pq esta fuera del IF")

my_other_condition = 5 * 2
if my_other_condition == 7:
    print("NO se ejecuta pq  5 * 2 = 10, y no 7")

if my_other_condition == 10:
    print("SI se ejecuta pq  5 * 2 = 10")


if my_other_condition >= 10:
    print("tambie se ejecuta pq  5 * 2 es mayor o igual q 10")


if my_other_condition > 10:
    print("Este tampoco pq no es mayor o igual que 10")
else: 
    print("NO es mayor o igual que 10")


my_condition = 6
my_other_condition = 3 * 5
if my_other_condition > 10 and my_condition < 5:
    print("Imprime, pq la other condition es mayor a 10 y mi condicion es menor que 5")
else: 
    print("NO se cumplen las condiciones")

my_condition = 2
my_other_condition = 3 * 5
if my_other_condition > 10 and my_condition < 5:
    print("Imprime, pq la other condition es mayor a 10 y mi condicion es menor que 5")
else: 
    print("NO se cumplen las condiciones")


if my_other_condition > 100 and my_condition < 5:
    print("Imprime, pq la other condition es mayor a 10 y mi condicion es menor que 5")
elif my_condition > 1 and my_other_condition > 1:
    print("NO SE CUMPLIO EL IF, pasa a el elseif")
else: 
    print("NO se cumplen las condiciones")

my_string = ""

if my_string:
    print("El string esta vacio (la cadena de texto está vacía")    # no immprime nada pq lo toma el string vacío como si fuera un "false"


my_string = "mi cadena de texto"

if my_string:
    print("El string esta con una cadena de texto")                 # ahora si lo imprime pq se cumple la condición pq esta como "true"

    my_string = "mi cadena de texto"

if my_string == "mi cadena de texto":
    print("El string esta con una cadena de texto 222")                 # tmb si lo imprime pq se cumple la condición coincide con la cadena de texto


if my_string == "mi cadena de textoooooo":
    print("El string esta con una cadena de texto 333")                 # no lo imprime pq se cumple la condición pq la cadena es diferente

if not my_string == "mi cadena de textoooooo":
    print("El string esta con una cadena de texto 333")                 # Esta vez is lo imprime pq el "not" hace q se cumpla la condicion




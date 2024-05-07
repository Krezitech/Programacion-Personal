# Temperatura:

print("Selecciona 1 si quieres convertir de F a C, selecciona 2 si quieres de C a F")
sel = int(input())
print("Selecciona la cantidad a convertir")
temp_inicial = float(input())

if sel ==1:
    temp_final = ((temp_inicial)-32)/1.8
    print("la temperatura ", temp_inicial, " F equivale a ",temp_final, " a C")
elif sel == 2:
    temp_final = (temp_inicial*(9/5))+32
    print("la temperatura ", temp_inicial, " C equivale a ",temp_final, " a F")
else:
    print("Escogiste una opción de conversión incorrecta") 

    
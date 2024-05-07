print("El PH se usa para saber si es ácida o básica una solución (0-14)")
ph = int(input("¿Cuál es el ph de tu solución? "))

if ph > 14:
    print("Diste un valor incorrecto fuera del margen")
elif ph < 0:
    print("Diste un valor incorrecto fuera del margen")
elif ph > 7:
    print("Tu solución es básica")
elif ph < 7:
    print("Tu solución es ácida")
elif ph > 14:
    print("Diste un valor incorrecto fuera del margen")
else: 
    print("Tu solución es Neutral")
# OPERADORES

print(3 + 6)
print(3 - 6)
print(3 * 6)
print(3 / 6)
print(10 // 3)  # Doble división - redondea al máximo número de divisiones, (opuesto a módulo)
print(10 % 3) # Módulo (%), o sea el sobrante de la divisioón
print(2**6) # 2 ^ 6

print("hola " + "Python")  # Puede sumar (concatenar) cadenas de texto (string)
#print("hola " + "Python" "Version " + 5) # NO se pueden "sumar" dos tipos diferentes (int + str)
print("hola " + "Python" "Version " + str(5)) # Si conviertes int a str, si se suman


print (2**3 + 3 - 7 / 1 // 4)  # Esto si sale pq es mismo tipo

print("x5 " * 5)  # Imprime "hola" 5 veces
print("x16 " * (2**4))  # Imprime "hola" 16 veces (2^4 veces)

mi_flotante = 3.5 * 2    # Se pueden definir variables flotantes 
print("whasup x7 " * int(mi_flotante))  # Pero para multimplicarlas hay que convertir en "int"

print(3 < 4)
print(3 > 4) 
print(3 <= 4)
print(3 >= 4)
print(3 == 4) # Igual
print(3 != 4) # Diferente

print("Van los comparadores de string")  # Se pueden comparar los "strings", resultado es buleano
print("comida" < "Python")   
print("comida" <= "Python")
print("comida" > "Python")
print("comida" >= "Python")
print("comida" == "Python")
print("comida" != "Python")

print("Ahora misma lenght")  
print("comida" == "temida")  # Sigue siendo falso
print("bola" == "bolb")  # Sigue siendo falso

print("Ahora Compara Alfabeticamente")
print("bola" >= "bolb")   # Este es falso
print("bola" <= "bolb")   # True pq la úlitma "b" es la que la hace "mayor"

print("Cuenta longitud")
print(len("hola") == len("coma"))   # Tienen misma longuitd así que es "True"

# Operadores lógicos 
print("Doble comparación")
print(3 > 4 and "hola" > "Python") 
print(3 > 4 or "hola" > "Python")
print(3 < 4 and "hola" <  "Python") 
print(3 < 4 or "hola"  > "Python")
print(3 < 4 or ("hola"  > "Python" and 4== 4)) # Prioridad en paréntesis

print("Usando NOT")
print(not(3 > 4) ) # Compara la condicion contra una negación



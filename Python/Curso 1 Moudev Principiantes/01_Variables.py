# Variables 

mi_variable = "Mi cadena variable"
print("mi_variable") # Si pones comillas, sera un string no variables 
print("Mi_Variable") # Es case sentivie
print(mi_variable)   # Las variables NO llevan nada, solo el nombre entre paréntesis

mi_variable_int = 34   # Asignar variables con otro tipo de dato
print(mi_variable_int)  

mi_variable_boleana = True   # Puede ser boleana también
print(type(mi_variable_boleana))

print(mi_variable_int, mi_variable, mi_variable_boleana)  # se pueden hacer cadenas de variables separadas por comas (Concaternar varuiables)

mi_int_to_str_variable = str(mi_variable_int) # Con "str" se puede cambiar una variable a tipo cadena

print(mi_int_to_str_variable) # Se imprime la variable ahora como cadena

print(type(mi_int_to_str_variable)) # Se puede ver el tipo, que ahora es cadena y no número


print(type(print(mi_variable_int, mi_variable, mi_variable_boleana) )) # No tiene type pq son varios tipos diferentes al mismo timpo

print(len(mi_variable))  # Da el "largo" de la variable, en este caso es 18 (mi_variable = "Mi cadena variable") 

print("Este valor es:",mi_variable_int) # Se puede concatenar texto con variables

name, surename, age, alias = "David Adrián", "Ochoa", 38, "Kreziped" # Se pueden agregar varias variables en un solo viaje

print("Hola, me llamo", name, surename,"tengo", age, "y en internet soy", alias) # se pueden hacer prints con texto y variables juntas

first_name = input('¿Cuál es tu nombre? ') # Con "input" se agregan datos a variables por usuario
age_2 = input("¿Cuántos años tienes? ") # Pueden ser string o int
print("tu nombre es:",first_name)
print("Tu edad es:", age_2)


forzar_variable: str = "mi texto de variable"  # Aunque se defina una variable como str
forzar_variable = True                         # Y luego se defina como boleano
forzar_variable = 454                          # Y aun despues se cambie a int
forzar_variable = 3.1416                       # Y finamente a flotante
print(type(forzar_variable))                   # siempre se actualiza al ultimo tipo de variable
 

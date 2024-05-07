# Strings

my_string = "Mi string"             # Funciona con comillas dobles
my_otherstring = 'Mi otro string'   # O con comillas simples

print(len(my_string))
print(len(my_otherstring))

print(my_string + " " + my_otherstring)     # se pueden sumar las strings

my_string_con_salto = "Los strings pueden tener saltos con diagonal n \ny va al otro" # \n salta línea

print(my_string_con_salto)


my_string_con_tab = "\t Los strings pueden tener espacios con diagonal t \ty va al otro" # \t espacio "tab"
print(my_string_con_tab)

my_string_sangria_salto = "\t Pones sangría y luego un \n salto"        # Se pueden mezclar
print(my_string_sangria_salto)


my_string_sangria_salto2 = "\\t Pones sangría y luego un \\n salto"        # Se con doble diagonal se anula
print(my_string_sangria_salto2)

# Formateo

name, surename, age = "David", "Adrián", 38         # Se declaran las variables

print("Yo soy " + name + " " +  surename + " y tengo " + str(age))           # Se puede hacer el print por variable

print("Mi nombre es: {} {} y tengo {} ".format(name,surename,age))  # Se puede usar format pero con llaves  

print("Me llamo: %s %s y tengo %d" %(name,surename,age))            # o bien % con la letra, funciona como seguro de que se use el tipo correcto, se usa para usar datos en varios idiomas por ejemplo

print(f"Me bautizaron como: {name} {surename} y tengo {age} ")      # La "f" ayuda a inferir y poder daler el formato (es la opción sugerida)

# Desempaquetado de caracteres

language = "python"             # Se define una variable   
a, b, c, d, e, f = language     # Esa variable se divide en diferentes variables
print(a)                        # Se imprimen las variables deseadas
print(b)
print(c)
print(d)
print(e)
print(f)

# División 

language_slice = language[1:3]      # Toma la siguiente del mínimo hasta la del máximo, uno es el inicio, empieza en 2, y hasta 3 que es el máximo "p YT hon"
print(language_slice)

language_slice = language[1:]      # Toma la siguiente del mínimo hasta el final
print(language_slice)

language_slice = language[-3]      # Toma la letra desde el final menos la dada "pyt H on"
print(language_slice)

language_slice = language[0:6:2]   # Toma desde cero, hasta 6, e imprime los caracteres de dos en dos     
print(language_slice)

# Reverse
print("Aquí comienza la reversa")

reverse_language = language[::-1]      # Lo escribe al revés
print(reverse_language)

# Funciones
print("Funciones")
print(language.capitalize())            # Pone la variable con mayúscula al inicio
print(language.upper())                 # Pone todo en mayúsculas
print(language.count("y"))              # Cuenta cuantas "Y" hay
print(language.isnumeric())             # Es un número?
print("1".isnumeric())                  # Es un número?
print(language.lower())                 # Todas minúsculas
print(language.upper().isupper())       # Primero pasa todo a mayúsculas y luego compara si es verdad
print(language.lower().isupper())       # Pasa todo a minúsculas y luego compara si es verdad
print(language.startswith("py"))        # "comienza con" verifica si es verdad (Verad)
print(language.startswith("Py"))        # "comienza con" verifica si es verdad (Falso)
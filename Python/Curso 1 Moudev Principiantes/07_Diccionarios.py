# Diccionarios

my_dict= dict()                     # Se puede definir de esta forma el tipo
print(type(my_dict)) 

my_other_dict = {}                  # O, tmb de esta forma
print(type(my_other_dict))

my_other_dict = {"Nombre":"David", "Apellido":"Adrian", "Edad":35, 1:"Python"}  # Clave-valor, se pueden asosciar datos, y tener una estructura de datos.

my_dict = {
    "Nombre":"David",
    "Apellido":"Adrian",
    "Edad":35,
    "Lenguajes":{"Python","CSS", "html"},
    1:1.74
    }                               # Se pueden visualizar también así, y la idea es formar datos asociados en un solo como en este caso, los lenguajes.

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))           # Tenemos definidos 4 elementos
print(len(my_dict))                 # Tenemos definidos 5 elementos

print(my_dict["Lenguajes"])         # Podemos acceder directamente a lo asociado dentro de la clave, en este caso, pone lo que son los "lenguajes" definidos

print(my_dict["Nombre"])
my_dict["Nombre"] = "Kreziped","Javco","David"      # Se puede reasignar de esta forma 
print(my_dict["Nombre"])                             # Ahora da estos valores

print(my_dict[1])                   # Para ver el entero, no se pueden comillas pq se definió como entero

my_dict["Calle"] = "Kreziroad"      # Se pueden agregar nuevos clave-valor
print(my_dict)

del my_dict["Calle"]                # Para borrar elementos se usa el "del" y lo que se va a borrar
print(my_dict)

print("David" in my_other_dict)              # Puede comprobar si existe en el dict, David Existe, es False pq aunque existe como valor, NO EXISTE COMO CLAVE  
print("Nombre" in my_other_dict)             # "Nombre" SI existe como clave, es True

print(my_other_dict)


print(my_dict.items())                      # Despliega todos los valores y los campos
print(my_dict.keys())                       # Muestra todas los campos
print(my_dict.values())                     # Muestra todos los valores

my_new_dict = my_other_dict.fromkeys(("Nombre",1))      # Crea un nuevo Diccionario, con las nuevas claves que se definen, en este caso "Nombre" y "1", pero no tienen valores
print(my_new_dict)                                      # Por eso sale como "None"

my_new_dict = dict.fromkeys(("Nombre",1, "Edad"))               # Pero puede simplemente usarse la palabra  reservada "dict" y crea lo mismo también     
print(my_new_dict)    


my_list = ["nombre", "apellido", "apodo"]               # hacer un diccionario desde una lista con fromkeys
my_newer_dict = dict.fromkeys(my_list)                  # Se agrega la lista y se crea un diccionario
print(my_newer_dict)

my_newer_dict = dict.fromkeys(("NOMBRE", "APELLIDO", "APODO"))      # o haciendolo directamente sin lista
print((my_newer_dict))

my_newer_dict = dict.fromkeys(my_dict)      # Se puede agregar un diccionario completo (vacío)
print((my_newer_dict))

my_newer_dict = dict.fromkeys(my_dict,("Valor1","Valor2"))          # Se ponen esos valores (1 y 2 a todos los elementos y no hay forma de poner un valor a una clave específica)     
print((my_newer_dict))

print(list(my_newer_dict))                  # Se pueden convertir en otra cosa como lista
print(tuple(my_newer_dict))                 # Se pueden convertir en otra cosa como tupla
print(set(my_newer_dict))                   # Se pueden convertir en otra cosa como set

print(my_newer_dict.values())               # Se pueden agregar Valores de todas las claves









# Sets

my_set = set()            # Palabra reservada, q es una función
print(type(my_set))         # Tipo de dato "set" 

my_other_set = {}               # Con solo llaves se crea un set también
print(type(my_other_set))       # Es un "diccionario"

my_other_set = {"David", "Kreziped", 35}   # Al agregar datos se vuelve "set"
print(type(my_other_set))                   # Ahora si es un "set" (En Python los datos pueden ser variables)

print(len(my_other_set))                    # se tienen 3 elementos

print(my_other_set)
#print(my_other_set[-1])                     # No se puede leer al revés como las listas

my_other_set.add("Nuevo")                   # Se pueden agregar elementos
print(my_other_set)                         # NO es una estructura ordenada, por eso el [-1] no funciona

my_other_set.add("Nuevo")                   # Se agrega nuevamente el elemento
print(my_other_set)                         # UN SET SOLO tiene valores únicos

print(my_other_set)                         # Cada itereación, el orden de "la lista" cambia

print("David" in my_other_set)              # Puede comprobar si existe en el set, David Existe, es True  
print("Daved" in my_other_set)              # Daved NO existe, es falso

print(my_other_set)   
my_other_set.remove("Nuevo")                # Se pueden quitar elementos
print(my_other_set)    

my_other_set.clear()                        # Se pueden limpiar las listas con "clear"
print(len(my_other_set))                    # Ahora es cero la longitud
print(my_other_set)                         # Sale vacía la lista

del my_other_set                            # Se puede borrar el set
#print(my_other_set)                         # Ya no lo encuentra pq no está definido, está borrado

my_set = {"David", "Kreziped", 35}          # Si se define un "set"
my_list = list(my_set)                      # Y luego se convierte a lista
print(type(my_list))                        # Ahora si es lista
print(my_list[2])                           # Ahora si se puede ver un elemento, PERO, la lista cambia en caada iteración porque el "set" varia siempre 

my_other_set = {"html", "css", "python"}    # Definimos un nuevo "set"

my_new_set = my_set.union(my_other_set)     # Con "union" se pueden junstar (concatenar)
print(my_new_set)                           # Cada iteración el orden cambia pq los "sets" cambian siempre

print(my_new_set.union({"C++", "Ensamblador"}))     # Se Pueden agregar directamente valores externos
print(my_new_set)                                   # Pero no se guardan en el "set" 

print("Las diferencias serán:")
print("my other set")
print(my_other_set)                         # Imprimimos my_other_set
print("myset")
print(my_set)                               # Imprimimos my_set
print("mi new set")
print(my_new_set)                           # Imprimimos my_new_set
print("Diferencia")
print(my_new_set.difference(my_set))        # Se imprime lo diferente entre my_new_set y my_set (se restan)



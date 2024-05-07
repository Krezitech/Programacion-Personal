# Listas

my_list =  list()          # Listas con paréntesis, la primera posición es la cero
my_other_list = []         # o tmb con corchetes

print(len(my_list))         # Da cero pq no hay nada

my_list =  [35, 24, 62, 52, 30, 30, 17]   # Una lista de edades por ejemplo
print(my_list)
print(len(my_list))         # Mumera la cantid de elementos (7)

my_other_list = [35, 1.74, "David", "Adrián"]       # Una lista puede tener diferentes tipos de datos
print(type(my_other_list))                          # El tipo es "list"
print(type(my_list))                                # El tipo es "list" aunque sea el que sea el tipo

print(my_other_list[0])         # Comienzan desde 0
print(my_other_list[1])         # Es el segundo item
print(my_other_list[-1])        # Es el ultimo
print(my_other_list[-3])        # El tercero desde el final
print(my_other_list[-4])        # Como la long es 4, pues pone el primero o el cuarto del final al inicio

print(my_other_list.count("David"))         # Cuenta el número de elementos q se repiten
print(my_list.count(30))                    # En la primer lista hay dos "30"

age, height, name, surename = my_other_list     # Puede igualarse a un arreglo, debe tener todos los elementos
print(name)                                     # Se puede imprimir ahora la nueva variable de un arreglo

name, height, age, surename = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]    # Puede re organizarse en otas listas con los num de corchetes, comenzando desde cero, para que hagan match de la lista original a un nuevo arreglo.
print(age)
print(surename)
print(height)
print(name)

print(my_list + my_other_list)          # Se pueden concatenar las listas

my_list = "Hola Python"                 # Se puede reasingar la lista y cambia su tipo
print(my_list)  
print(type(my_list))                    # Ahora es "str"

my_list = ["Hola Python"]               # Si se usan corchetes o "list()"
print(my_list)  
print(type(my_list))                    # Ahora es lista

my_other_list.append("Kreziped")        # Se pueden agregar nuevos elementos con "append"
print(my_other_list)

my_other_list.insert(1, "Azul")         # Con "insert", se pueden agregar elementos en la posición dada
print(my_other_list)

my_other_list.remove("Azul")            # Con "remove", se pueden eliminar elementos
print(my_other_list)

my_list =  [35, 24, 62, 52, 30, 30, 17]     # Se define una lista
print(my_list)
my_list.remove(30)                          # Se elimina solo un elemento, no todos
print(my_list)

my_list.pop()                           # Elimina el úlitmo elemento
print(my_list)
my_list.pop()                           # Borra el "52"
print(my_list)
print(my_list.pop())                    # En este caso es "52" el elementp que borró al final

my_pop_element = my_list.pop(2)         # Se puede reasignar o "sacaqr" un elemento particular la tercera posición (2), equivale al 62 en nuestra lista (linea 53)
print(my_pop_element)

print(my_list)

del my_list[0]                          # Se pueden borrar directamente con "Del" y la posición

print(my_list)

my_list =  [35, 24, 62, 52, 30, 30, 17] # Redefiniendo la lista
print(my_list)
my_list.clear()                         # Se puede borrar, Del borra todo, REMOVE quita algo especifico
print(my_list)


my_other_list.insert(1, "Azul")        
print(my_other_list)

my_other_list[1] = "Rojo"               # Se pueden editar por posición en el arreglo
print(my_other_list)

my_list =  [35, 24, 62, 52, 30, 30, 17]     # Se define una lista
print(my_list)
my_new_list = my_list                       # Se asigna una lista a otra lista
my_newer_list = my_list.copy()              # Se copia una lista a nueva lista
my_list.clear()                             # Se limpia la lista

print(my_list)                              # Sale vacía pq se limpió
print(my_new_list)                          # Sale vacía pq depende de la lista (se asignó)
print(my_newer_list)                        # Tiene los valores de la lista original pq se copió

my_newer_list.reverse()                     # Se ponen los items "al revés"
print(my_newer_list)

my_newer_list.sort()                        # Se ordena una lista (deben ser números)
print(my_newer_list)

print(my_newer_list[1:3])                   # Imprime las posciones de las listas dadas
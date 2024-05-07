# Tuplas

my_tuple = tuple()         # Se definen de dos formas, con "tuple"
print(type(my_tuple))
my_other_tuple = ()        # o simplemente con paréntesis

my_tuple =(35, 1.74,"David", "Adrian")
print(my_tuple)
print(type(my_tuple))       # Tipo Tupla

print(my_tuple[0])          # De igual forma comienza en el 0
print(my_tuple[-1])         # Pondría el último

print(my_tuple.count("David"))      # Cuenta cuantas veces se repite como en las listas
print(my_tuple.index("David"))      # Da el lugar de la "lista" que ocupa el campo seleccionado

#my_tuple[1]=1.80                    # NO deja cambiar variables, las definidas se quedan estáticas
print(my_tuple)

#my_tuple[5]=1.80                   # Tampoco deja agregar nuevos "items" a la lista original

my_other_tuple = (35, 60, 30)       # Se pueden crear muchas tuplas
print(my_tuple + my_other_tuple)    # Se pueden "sumar" las tuplas
my_sum_tuples = my_tuple + my_other_tuple   # Se pueden concatenar
print(my_sum_tuples)
print(my_sum_tuples[3:6])           # Se pueden imprimir los valores 3 al 5

my_tuple =  list(my_tuple)          # Una tupla se puede redefinir como una lista
print(type(my_tuple))               # Es una lista ahora!!!

my_tuple[3] = "kreziped"            # Como lista ya se puede redefinir
my_tuple.insert(1,"Azul")           # Incluso agregar elementos
print(my_tuple)

my_tuple = tuple(my_tuple)          # Se puede reasignar nuevamente una lista ahora como tupla
print(type(my_tuple))

del my_tuple                        # Se elimina la Tupla (NO el contenido)
#del my_tuple[2]                     # Tampoco se pueden borrar elementos de una tupla
#print(my_tuple)                     # Manda error porque ya NO existe la variable


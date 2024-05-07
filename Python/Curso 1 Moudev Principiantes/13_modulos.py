##########################################################
#################        Moódulos       ##################
##########################################################

print(" ")
print("#################################################")
print("#################      1      ###################")
print("#################################################")
print(" ")

import my_module               # Se importa un módulo con "import" y luego el nombre del modulo,

my_module.sumValue(3,5,5)          # Se pone el nombre del modulo.lafuncion para llamarla y luego ya usarla normal

my_module.printValue("Imprimirá esto")      # Ahora busca la funcion "#printValue" y trabaja con ella

print(" ")
print("#################################################")
print("#################      2      ###################")
print("#################################################")
print(" ")

from my_module import sumValue          # Importa únicamente la funcion "suma" de "my_module"

sumValue(13,7,21)               # Suma funciona bien pq esta importada, ya no require el punto

#my_module.printValue("Imprimirá esto")   # Pero esta no, pq no se importó

print(" ")
print("#################################################")
print("#################      3      ###################")
print("#################################################")
print(" ")

from my_module import sumValue, printValue          # Importa ambas funciones

sumValue(3,8,11)               # Suma funciona bien pq esta importada

printValue("Imprimirá esto")   # Esta también, pq  se importó

print(" ")
print("#################################################")
print("#################      4      ###################")
print("#################################################")
print(" ")

import math

print(math.pi)
print(math.sqrt(64))
print(math.pow(2,8))

from math import pi as PI_Value         # Se puede importar directamente como una variable
print(PI_Value)                         # Se imprime la variable
##########################################################
#################      Excepciones      ##################
##########################################################

# Se usan para en caso de errores, el programa no muera, sino contenga el problema
print(" ")
print("#################################################")
print("#################      1      ###################")
print("#################################################")
print(" ")

numero1 = 5
numero2 = "5"

#print(numero1 + numero2)              # No puede sumarlos pq uno es "str" y el otro "int"


print(" ")
print("#################################################")
print("#################      2      ###################")
print("#################################################")
print(" ")

# con el "try" intenta realizar lo solicitado, y con "except", crea un camino alterno en caso de que el "try" no pueda ejecutarse


numero1 = 5
numero2 = "5"

try:
    print(numero1 + numero2)                # No se pudo, pq el num2 es "str"
except:
    print("Hubo un error en la suma")       # Despliega este texto al no habers podido anteriormente



numero3 = 5
numero4 = 5

try:
    print(numero3 + numero4)                # como son los dos "int", se realiza y despliega lo solicitado
    print("No hubo error!!!")   
except:
    print("Hubo un error en la suma")       # No aplica pq si se pudo realizar la acción


print(" ")
print("#################################################")
print("#################      3      ###################")
print("#################################################")
print(" ")


numero1 = 5
numero2 = 5

try:
    print(numero1 + numero2)                         # se ejecuta pq no pasa una excepcion
    print("No hubo error!!!")                        # se ejecuta pq no pasa una excepcion

except:
    print("Hubo un error en la suma")   

else:
    print("La ejecución continúa correctamente")    # se ejecuta pq no pasa una excepcion  

print(" ")
print("#################################################")
print("#################      4      ###################")
print("#################################################")
print(" ")

numero1 = 5
numero2 = 5

try:
    print(numero1 + numero2)                         # se ejecuta pq no pasa una excepcion
    print("No hubo error!!!")                        # se ejecuta pq no pasa una excepcion

except:
    print("Hubo un error en la suma")   

else:
    print("La ejecución continúa correctamente")    # se ejecuta pq no pasa una excepcion   

finally:
    print("Continua y continua")                    # Igual se ejectuta pq es "al final de todo"

print(" ")
print("#################################################")
print("#################      5     ####################")
print("#################################################")
print(" ")

numero1 = 5
numero2 = "5"

try:
    print(numero1 + numero2)
    print("No hubo error!!!")

except:
    print("Hubo un error en la suma")               # Se ejecuta pq hay un error

else:
    print("La ejecución continúa correctamente")

finally:
    print("Continua y continua")                    # Igual se ejectuta pq es "al final de todo", SIEMPRE

print("Esto ya esta fuera del código")

print(" ")
print("#################################################")
print("#################      6     ####################")
print("#################################################")
print(" ")

# Excepciones por tipo (Type)
# busca un tipo de error determinado, ejemplo "type", pero puede tener varios "ValueError"

numero1 = 5
numero2 = "5"

try:
    print(numero1 + numero2)
    print("No hubo error!!!")

except  ValueError:
    print("Hubo un error en el tipo (Value)")

except  TypeError:
    print("Hubo un error en el tipo (Type)")

print(" ")
print("#################################################")
print("#################      7     ####################")
print("#################################################")
print(" ")

# Captura de la información de la excepción

numero1 = 5
numero2 = "5"

try:
    print(numero1 + numero2)
    print("No hubo error!!!")

except  TypeError as error:             # Encuentra el error en este caso es de type y lo asigna a la var "error"        
    print(error)

print(" ")
print("#################################################")
print("#################      8     ####################")
print("#################################################")
print(" ")

# Captura de la información de la excepción

numero1 = 5
numero2 = "5"

try:
    print(numero1 + numero2)                         
    print("No hubo error!!!")    

except Exception as errororifico:       # También se puede hacer, si es una excepción sea cual sea, la asigne a la variable "errorifico"
    print(errororifico)
 
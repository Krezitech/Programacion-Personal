# Funciones

# Las funciones van a resolver un problema determinado y la idea es de poderla llamar cuando se requiera

def  my_function ():
    print("Esto es una función")

my_function()

def sumatoriados (numero1, numero2):        # se definen dos cosas
    print(numero1 + numero2)                # se hace la suma de la función

sumatoriados(33,77)                         # se llama la funcion con diferentes parametros
sumatoriados(51,44)                         # se llama la funcion con diferentes parametros
sumatoriados(456112,230412)                 # se llama la funcion con diferentes parametros


def sumatoriados (numero1, numero2):       
    print(numero1 + numero2)                

resul = sumatoriados(3.5,5)                 # Imprime el resultado
print(resul)                                # Pero la variable es "none"


numero1 = float(input("Dame el primer número a sumar: "))
numero2 = float(input("Dame el segundo número a sumar: "))
sumatoriados(numero1,numero2) 

sumatoriados("44","88")                     # Para los "str", solo concatena = 4488   
#sumatoriados("3",5)                        # Este no lo pasa pq no son del mismo tipo
sumatoriados(3.5,5)                         # Aqui aunq sea "float" y el otro "int", se puede pq son numeros

def sum_dos_valores_con_return (primero,segundo):
    return primero + segundo

resultado = sum_dos_valores_con_return(15, 88)  # Asigna la variable

print(resultado)                                # Imprime la variable
print(resultado)                                # Imprime la variable

 


def sum_dos_valores_con_return (primero,segundo):
    la_suma = primero + segundo
    return la_suma

def print_nombre (nombre, apellido):
    print(f"{nombre} {apellido}")

print_nombre("Ochoa","David")       # Si se le da directamente, los pone en orden de inserción
print_nombre(apellido = "Ochoa",nombre = "David")       # Si se da asignación, lo respeta


def print_nombre_default (nombre, apellido, alias):    # Paramétros por defecto se deben dar todos
    print(f"{nombre} {apellido} {alias}")

print_nombre_default("David", "Ochoa", "Kreziped")      # Aquí se ve que están todos los campos


def print_nombre_default (nombre, apellido, alias = "Sin alias"):   # Así se asigna un valor por default
    print(f"{nombre} {apellido} {alias}")

print_nombre_default("David", "Ochoa")                           # y, si no hay valor, pone el default     


def print_textos (text):            # Se le da una variable
    print(text)                     # Imprime la variable

print_textos ("Hola!!!")            # puede tener una


def print_textos (*text):            # Se le da una variable pero con * antes
    print(text)                     # Imprime la o las variables

print_textos ("Hi")                       # puede tener una o mas
print_textos ("Hi", "Aloha", "Bonjour")    # Imprime todas



def print_textos (*texts):                  # Se le dice que va a imprimir varios
    for text in texts:                      # Con el for, va imprimendo cada uno de la lista en cada iteración  
        print(text)                         # Va imprimiendo la lista

print_textos ("Hi", "Aloha", "Bonjour")     # En este caso imprime una lista de 3



def print_mayus_textos (*texts):                  
    for text in texts:                       
        print(text.upper())              # Mantiene las propiedades de los textos                         

print_mayus_textos ("Hi", "Aloha", "Bonjour")       # Los imprime ahora en mayúsculas    
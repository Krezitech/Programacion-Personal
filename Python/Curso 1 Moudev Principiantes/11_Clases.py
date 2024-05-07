# Clases

# Una clase tiene q tener cosas relacionadas con la clase, ejmplo clase = persona, variables bien seria "dormir", una que no cuadra sería "avión"

class MyPersonaVacia:              # OJO que lleva mayúscula al inicio las clases
    pass 

print(MyPersonaVacia)
print(MyPersonaVacia())

class MyPersona2:
    def __init__(self) -> None:         # "init" es un contructor de clase, o sea que reciba un parámetro
        pass

class Persona:
    def __init__(self, name, surename):     # Se le dan las clases a utilizar (nombre y apellido)
        self.name = name                    # Se asigna la variable a self
        self.surename = surename

my_persona = Persona("David", "Ochoa")      # se ponen los valores
print(f"{my_persona.name} {my_persona.surename}")   # Se imprimen con las asignaciones

class Persona:
    def __init__(self, name, surename):
        self.full_name = f"{name} {surename}"   # O bien se agrega todo como una especie de función

my_persona = Persona("Adrian", "Gaona")         # se ponen los valores
print(my_persona.full_name)                     # se imprime la función (linea 26)




class Persona:
    def __init__(self, name, surename):
        self.full_name = f"{name} {surename}"   

    def walk(self):                                 # Dentro de la clase se puede pueen poner mas funciones
        print(f"{self.full_name} Está caminando")   # y dentro de esta se peude mandar a llamar con el self


my_persona = Persona("Adrian", "Gaona")         
print(my_persona.full_name)                         # Imprime esto              
my_persona.walk()                                   # Tmb esto


print("#################################################")
print("#################      1      ###################")
print("#################################################")

class Persona:
    def __init__(self, name, surename, alias = "Sin Alias"):
        self.full_name = f"{name} {surename} ({alias})"         # Ahora el alias saldrá entre ()   

    def walk(self):                                 
        print(f"{self.full_name} Está caminando")   


my_persona = Persona("Adrian", "Gaona")         
print(my_persona.full_name)                                     
my_persona.walk()                                  

my_other_person = Persona("Ben", "De Jong", "Benxito")      # Pone el alias
print(my_other_person.full_name)                            # Ahora imprime todo con alias
my_other_person.walk()        

my_other_person.full_name = "Raúl González (El ángel de Madrid)"    # Ya que se definiio ya se puede reestrables q lo q se desee    
print(my_other_person.full_name)                                    # Imprime nuevos valores de la variable

my_other_person.full_name = 666                 # NO se pone el alias con el cambio, YA SE ROMPIO LA CLASE
print(my_other_person.full_name)                # NO se imprime el alias, ya es otra cosa    

print("#################################################")
print("#################      2      ###################")
print("#################################################")


class Persona:
    def __init__(self, name, surename, alias = "Sin Alias"):
        self.full_name = f"{name} {surename} ({alias})"
        self.__name = name                                      # lo hace privad
        self.__surename = surename                              # lo hace privad

    def get_name(self):                                         # Entocnes para poderlo ver hay q crear un get
        return self.__name                                      # y que "return" ese valor
       
my_persona = Persona("Adrian", "Gaona")         
print(my_persona.full_name)                                     
print(my_persona.get_name())                                    # Arhoa si se puede imprimir    


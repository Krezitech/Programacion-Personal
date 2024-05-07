##########################################################
#################         Dates        ###################
##########################################################

print(" ")
print("#################################################")
print("#################      1      ###################")
print("#################################################")
print(" ")

from datetime import datetime               # Se agrega el "módulo" de "datetime"

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp()

print(timestamp)
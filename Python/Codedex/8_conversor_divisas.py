# Conversor de divisas

print("Fuiste de vacaciones a Europa y te sobraron Libras por ir a Gran Bretaña, Euros por el resto de Europa y dólares porque hiciste escala en Estados Unidos")
print("El cambio de 1 Libra a pesos mexicanos es: 22.86")
print("El cambio de 1 Euro a pesos mexicanos es: 20.48")
print("El cambio de 1 Dólar a pesos mexicanos es: 18.97")
print("Para saber cuánto dinero tienes, llena el formulario siguiente:")
libra = float(input("¿Cuántas Libras tienes: "))
euro = float(input("¿Cuántos Euros tienes: "))
dolar = float(input("¿Cuántos Dólares tienes: "))

plibra = libra * 22.86
peuro = euro * 20.48
pdolar = dolar * 18.97
total = plibra+pdolar+peuro

print("Las Libras que tienes equivalen a ",plibra, " pesos")
print("Los Euros que tienes equivalen a ",peuro, " pesos")
print("Los Dólares que tienes equivalen a ",pdolar, " pesos")
print("El total de todo el dinero que tienes es: ",total)
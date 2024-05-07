# Programa para sacar las raices de la fórmula general

print("Una fórmula cuadrática tiene la forma: ax^2+bx+c=0")
print("Para resolver, introduce las variables que se te solicitan:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

x1 = (-b+(b**2-(4*a*c))**0.5)/(2*a)
x2 = (-b-(b**2-(4*a*c))**0.5)/(2*a)

print("La una de las raices es: ",x1)
print("La otra raíz es: ",x2)
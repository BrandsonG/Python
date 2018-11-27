Num1 = int(input("Pon el dividendo:"))
Num2 = int(input("Pon el divisor:"))

Resto = Num1%Num2

if(Num1%Num2==0):
    print("El resto es", Resto, "Divison exacta")
else:
    if(Num1%Num2>0):
        print("El resto es", Resto, "Division no exacta")


#Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.
#DIVISOR DE NÚMEROS
#Escriba el dividendo: 14
#Escriba el divisor: 5
#La división no es exacta. Cociente: 2 Resto: 4


#DIVISOR DE NÚMEROS
#Escriba el dividendo: 20
#Escriba el divisor: 4
#La división es exacta. Cociente: 5


#Nota: Se puede mejorar el programa haciendo que tenga en cuenta que no se puede dividir por cero:
#DIVISOR DE NÚMEROS
#Escriba el dividendo: 20
#Escriba el divisor: 0
#No se puede dividir por 0

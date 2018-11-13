#coding:utf-8
opcio=input("Que quieres calcular T o C:")
if(opcio=="T"):
    base_triangulo=int(input("Base triangulo:"))
    altura_triangulo=float(input("Altura triangulo:"))
    Res=abs(base_triangulo*altura_triangulo/2)
    print("El área es",Res)
else:
    pi=3.14159265359
    radio_circulo=int(input("Radio circulo:"))
    Res_2=abs(2*pi*radio_circulo)
    if(opcio=="C"):
        print("Area del circulo es",Res_2)

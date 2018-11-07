#coding: utf-8

anyo_actual=int(input("En que año estamos?"))
anyo_cualquiera=int(input("Introduce un año:"))
Resultado=abs(anyo_actual-anyo_cualquiera)

if (anyo_actual >=2018) and (anyo_cualquiera >2018):
    print("Para llegar al año", anyo_actual,"faltan", Resultado,"años");
else:
    if (anyo_actual == anyo_cualquiera):
        print("Son el mismo año!");
    else:
        if (anyo_cualquiera >2018) and (anyo_actual == 2018):
            print("Desde el año", anyo_actual,"han pasado", Resultado,"años");
            

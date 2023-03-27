A:float #variable A como flotante
año:float #variable B como flotante
A = 25000000 #iniciar variable A en 25000000
B = 18900000 #iniciar variable B en 18900000
año = 2022 #iniciar año en 2022
while (A>B): #Mientras A sea mayor que B
    A*= 1.02 #multiplicar A por 1.02 para tener el incremento del 2%
    B*= 1.03 #multiplicar A por 1.03 para tener el incremento del 3%
    año += 1 #Revaluamos el año 
print("La población de del país B superará a la del país A en el año: " +str(año)) #imprimimos en que año la variable B supera a la variable A


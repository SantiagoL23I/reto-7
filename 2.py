x:float #primera variable como flotante
y:float #segunda variable como flotante
x=1 #iniciar variable en 1
y=2 #iniciar variable en 2
while (y<=1000): #mientras la variable sea menor o igual que 1000 se mantendra el ciclo
    if (y%2==0): #condición donde el residuo entre la variable y 2 es 0 
        print ("Los numero pares son: " +str(y)) #imprmir la variable y
    y+=1 #actualizar al siguiente número
while (x<=999): #mientras la variable sea menor o igual que 999 se mantendra el ciclo
    if (x%2!=0): #condición donde el residuo entre la variable y 2 es mayor que 0
        print ("Los numero impares son: " +str(x)) #imprimir la variable x
    x+=1 #actualizar al suguiente número
x= int(input("Ingrese un número: ")) #pedir ingresar un número al usuario para la variable entera 
while (x>=2): #mientras la variable sea mayor o igual que 2 se mantendra el ciclo
    if x%2!=0: #condición donde el residuo entre la variable y 2 es diferente que 0 (impar)
        x-=1  #restar 1 a la variable para que se convierta en par 
    print(x) #imprimir la variable
    x-=2   #actualizamos a los dos anteriores números para que siga en par y sea descendente      
        
    
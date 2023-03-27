n=int(input("ingrese un número: ")) #pedir ingresar un número al usuario para la variable entera 
x:int #variable x como entera
x = n #iniciar la variable x en n
while (n>1): #mientras n sea mayor que 1
    n-=1 #restar 1 a n para multiplicarlo por el numero anterior digitado
    x*=n #multiplicamos x por n 
print("El factorial es: "+str(x)) #imprimimos el resultado

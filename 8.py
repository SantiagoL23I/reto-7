def primo(x : int, i = int)->int: #definimos "primo" como funcion con reultado entero 
        i = 2  # iniciar variable n en dos
        if x == 2 : #condicion donde la variable x es igual a 2 
            print(x) #imprimir la variable x
        while i != x : #mientras i sea diferente a n
            if x%i == 0: #condición donde el residuo entre la variable "x" y "i" es 0
                break #rompe el ciclo
            elif i == x-1: #condicion diferente, donde i es igual a x-1 para evaular otro valor en el ciclo hasta que se rompa
                print(x) #imprimir la variable x
            i += 1 #actualizar al siguiente número

if __name__ == "__main__" : 
    x = int #variable x como entera
    x = 2 #iniciar variable x en 2
    f = 100 #iniciar variable f en 100
    while x < f: #mientras n sea menor que f
        a = primo(x) #llama la funcion primo
        x += 1 #actualizar al siguiente numero 

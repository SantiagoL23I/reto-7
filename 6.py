print("Piensa en un número entre 1 y 100.") #imprimir texto para que el usuario lo vea
print("Solo responde con 'mayor', 'menor' o 'sí'") #imprme el texto de como debe responder el ususario
x:int #variable x como entero
y:int #variable y como entero
r:str #variable r como string
x = 1 #iniciar variable en uno
y = 100 #iniciar variable en cien

while True: #mientras sea verdadero
        t=x+y//2 #Primer valor sea la suma de "x" y "y" dividido por 2
        r = input("Es " +str(t)+" tu número? ") #pregunta si el primer valor es el numero
        if r == "sí": #condicion donde r es igual a sí
            print("Adiviné el número") #imprime el texto de que se adivino el número
            break #se rompe el ciclo
        elif r == "mayor": #condicion donde r es igual a mayor
            x = x + (y - x) // 3 #se ajusta el rango a un tercio entre el rango anterior y la mitad actual
        elif r == "menor": #condicion donde r es igual a menor
            y = x + (y - x) // 2 #se ajusta el rango a la mitad del anterior 
        else: #condicion en caso que no se cumpla 
            print("Solo responde con 'mayor', 'menor' o 'sí'") #imprme el texto de como debe responder el ususario

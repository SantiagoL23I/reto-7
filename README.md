
# Reto 7

#### 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```pseudocode
x: float #variable como flotante
x= 1 #iniciar variable x en 1
while (x <=100): #mientras la variable sea menor o igual que 100 se mantendra el ciclo
    print("el cuadrado de:" +str(x)+ " es " +str(x**2)) #imprimir el número y su cuadrado
    x+=1 #actulizar al siguiente entero
```
[![](https://mermaid.ink/img/pako:eNo9j0FzgjAQhf9KZk9qwSFGIKS1Jy89t6dCDzEJkBlIHAxTlOG_N1owp_e9vN03O4KwUgGDsrG_ouadQ1_H18Ig__jqw2ih7RqF4Ts65cPBh7j7mb9FPiDVnrW6caQMwosvx-HtgKNomlnlqkGi57Lj0iJ1YUuwys1ms1uoXpXarGco8-HlufDk68VS6rVcisLwoj2rpcjrclngdTXX3Ece8jGAjPVG7XMQQKu6lmvp7x_viQJcrVpVAPNSqpL3jSugMJOP8t7Zz6sRwEreXFQA_Vlyp46aVx1vn-6Zm29rPbuu_0dgIwzAMI23hFCME0KSaIczEsAVWJhuM5JSEmeY7kmU0ngK4PbYEG29Q7OYkhQnyX6_I9MfJQJ7Og?type=png)](https://mermaid.live/edit#pako:eNo9j0FzgjAQhf9KZk9qwSFGIKS1Jy89t6dCDzEJkBlIHAxTlOG_N1owp_e9vN03O4KwUgGDsrG_ouadQ1_H18Ig__jqw2ih7RqF4Ts65cPBh7j7mb9FPiDVnrW6caQMwosvx-HtgKNomlnlqkGi57Lj0iJ1YUuwys1ms1uoXpXarGco8-HlufDk68VS6rVcisLwoj2rpcjrclngdTXX3Ece8jGAjPVG7XMQQKu6lmvp7x_viQJcrVpVAPNSqpL3jSugMJOP8t7Zz6sRwEreXFQA_Vlyp46aVx1vn-6Zm29rPbuu_0dgIwzAMI23hFCME0KSaIczEsAVWJhuM5JSEmeY7kmU0ngK4PbYEG29Q7OYkhQnyX6_I9MfJQJ7Og)
#### 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```psudocode
x:float #primera variable como flotante
y:float #segunda variable como flotante
x=1 #iniciar variable x en 1
y=2 #iniciar variable y en 2
while (y<=1000): #mientras la variable sea menor o igual que 1000 se mantendra el ciclo
    if (y%2==0): #condición donde el residuo entre la variable y 2 es 0 (par)
        print ("Los numero pares son: " +str(y)) #imprmir la variable y
    y+=1 #actualizar al siguiente número
while (x<=999): #mientras la variable sea menor o igual que 999 se mantendra el ciclo
    if (x%2!=0): #condición donde el residuo entre la variable y 2 es diferente que 0 (impar)
        print ("Los numero impares son: " +str(x)) #imprimir la variable x
    x+=1 #actualizar al suguiente entero
```
#### 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```psudocode
x= int(input("Ingrese un número: ")) #pedir ingresar un número al usuario para la variable entera 
while (x>=2): #mientras la variable sea mayor o igual que 2 se mantendra el ciclo
    if x%2!=0: #condición donde el residuo entre la variable y 2 es diferente que 0 (impar)
        x-=1  #restar 1 a la variable para que se convierta en par 
    print(x) #imprimir la variable
    x-=2   #actualizamos a los dos anteriores números para que siga en par y sea descendente      
```
#### 4. En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18:9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

```psudocode
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
```
#### 5.Imprimir el factorial de un número natural n dado.
 
```psudocode
n=int(input("ingrese un número: ")) #pedir ingresar un número al usuario para la variable entera 
x:int #variable x como entera
x = n #iniciar la variable x en n
while (n>1): #mientras n sea mayor que 1
    n-=1 #restar 1 a n para multiplicarlo por el numero anterior digitado
    x*=n #multiplicamos x por n 
print("El factorial es: "+str(x)) #imprimimos el resultado
```
#### 6. Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.

```psudocode
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
```
#### 7. Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.
```psudocode
n=float(input("ingrese un número entre el 2 y el 50: ")) #pedir ingresar un número al usuario para la variable n flotante
x:float #variable x como flotante
x=1 #iniciar la variable x en 1
while (n>=2 and n<=50 and x<=n ): #mientras n sea mayor o igual que 2, menor igual que 50 y mayor igual que x
    if n%x == 0: #condición donde el residuo entre la variable "x" y "n" es 0
     print(x) #imprimimos la variable x
    x+=1 #actualizamos al siguente entero
```
#### 8. Implementar el algoritmo que muestre los números primos del 1 al 100. nota: use funciones

```psudocode
def primo(x : int, i = int)->int: #definimos "primo" como funcion con reultado entero 
        i = 2  # iniciar variable n en dos
        if x == 2 : #condicion donde la variable x es igual a 2 
            print(x) #imprimir la variable x
        while i != x : #mientras i sea diferente a n
            if x%i == 0: #condición donde el residuo entre la variable "x" y "i" es 0
                break #rompe el ciclo
            elif i == x-1: #condicion donde i es igual a x-1 para evaular otro valor en el ciclo hasta que se rompa
                print(x) #imprimir la variable x
            i += 1 #actualizar al siguiente número

if __name__ == "__main__" : 
    x = int #variable x como entera
    x = 2 #iniciar variable x en 2
    f = 100 #iniciar variable f en 100
    while x < f: #mientras n sea menor que f
        a = primo(x) #llama la funcion primo
        x += 1 #actualizar al siguiente entero
```

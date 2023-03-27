n=float(input("ingrese un número entre el 2 y el 50")) #3
x:float
x=1
while (n>=2 and n<=50 and x<=n ):
    if n%x == 0:
     print(x)
    x+=1
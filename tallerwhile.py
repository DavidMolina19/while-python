
print("1.suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")
print("5.potenciacion")
print("6.raiz cuadrada")
print("7.cambiar numeros")
print("8.salir")


operacion=int(input("que operacion deseas realizar?: "))
print("la raiz cuadrada debe ser numero positivo y entero")
n1=int(input("ingrese el valor 1: "))
n2=int(input("ingrese el valor 2: "))

while operacion!=7:
    if operacion==1:
        print("la suma es ", n1+n2)
    elif operacion==2:
        print("la resta es ", n1-n2)
    elif operacion==3:
        print("la multiplicacion es: ", n1*n2)
    elif operacion==4 and n2==0:
        print("no se puede realizar la operacion por 0")    

    elif operacion==4 and n2!=0:
        print("la division es ", n1//n2)
    elif operacion==5:
        print("la potenciacion es ", n1**n2)
    elif operacion==6:
        
        a=n1**0.5
        b=n2**0.5
        print("la raiz cuadrada del numero 1 es ", a)     
        print("la raiz cuadrada del numero 2 es ", b)  
    elif operacion==7:
          n1=int(input("ingrese el valor 1: "))
          n2=int(input("ingrese el valor 2: "))
    elif operacion==8:
        print("salir")
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.division")
    print("5.potenciacion")
    print("6.raiz cuadrada")
    print("7.cambiar numeros")
    print("8.salir")

    operacion=int(input("que operacion deseas realizar?: "))
    n1=int(input("ingrese el valor 1: "))
    n2=int(input("ingrese el valor 2: "))
    






    

def calculadora():
    global num1, num2
    num1 = int(input("Introduzca el primer numero:"))
    num2 = int(input(" Introduzca el segundo numero:"))

def sumar(num1=0, num2=0):
    print("El resultado es =", num1+num2)

def restar(num1=0, num2=0):
    print("El resultado es =", num1-num2)

def multiplicar(num1=0, num2=0):
    print("La multiplicacion es = ", num1*num2)

def division( num1, num2):
    if num2 == 0:
            print("LA division no puede divir entre 0")
    else:
        print("La division de=", num1/num2 )










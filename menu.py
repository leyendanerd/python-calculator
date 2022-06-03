from funciones import *
from funciones import num1, num2

while True:
    print("""
    Indique la operacion a realizar: 

    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Salir de la calculadora
    """)

    eleccion= int(input("opcion:"))

    if eleccion == 1: 
       calculadora()
       sumar(num1, num2)

    elif eleccion == 2: 
       calculadora()
       restar(num1, num2)

    elif eleccion == 3: 
       calculadora()
       multiplicar(num1, num2)

    elif eleccion == 4: 
       calculadora()
       division(num1, num2)

    elif eleccion == 5: 
       print("Hasta pronto")
       break




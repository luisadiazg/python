"""
Created on Tue Sep  4 19:50:53 2018

@author: Luis Díaz G. (deshack)
"""

def compara(num1,num2):
    if (num1>num2):
        print ("El numero " , num1 , " es mayor que el numero ", num2, "\n")
    else:
        if (num2>num1):
            print ("El numero " , num2 , " es mayor que el numero ", num1, "\n")
        else:
            print ("Los numeros son iguales \n")

print ("Programa de comparacion mayor menor \n")
numero1=int(input("Ingrese un numero para comparar \n"))
numero2=int(input("Ingrese un numero para comparar \n"))
compara(numero1,numero2)

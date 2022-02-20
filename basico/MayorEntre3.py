"""
Created on Tue Sep  4 19:50:53 2018

@author: Luis Díaz G. (deshack)
"""

def mayor(n1,n2,n3):
    if (n1>n2):
        mayor=n1
    if (n2>n1):
        mayor=n2
    if (n1>n3):
        mayor=n1
    else:
        mayor=n3
    print ("el numero mayor es ", mayor, "\n")

print ("Programa de comparacion mayor menor \n")
n1=int(input("Ingrese un numero para comparar \n"))
n2=int(input("Ingrese un numero para comparar \n"))
n3=int(input("Ingrese un numero para comparar \n"))
mayor(n1,n2, n3)

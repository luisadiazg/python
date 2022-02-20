def suma(n1,n2):
    suma = n1+n2
    return suma

def resta(n1,n2):
    resta = n1-n2
    return resta

def mult(n1,n2):
    multiplicar = n1 * n2
    return multiplicar

def div(n1,n2):
    dividir = (n1 / n2)
    return dividir

def potencia(n1,n2):
    potencia = n1 ** n2
    return potencia


print("Ingrese dos números para operar")
print("")
num1 = int(input("ingrese numero 1 :  "))
num2 = int(input("ingrese numero 2 :  "))
res_sum  = suma(num1,num2)
res_rest = resta(num1,num2)
res_mult = mult(num1,num2)
res_div  = div(num1,num2)
res_pot  = potencia(num1,num2)

print ("El resultado de la adición es : " , res_sum)
print ("El resultado de la sustracción es : " , res_rest)
print ("el resultado de la multiplicacion es : " ,  res_mult)
print ("El resultado de la division es : " , res_div)
print ("El resultado de la potencia es : " , res_pot)

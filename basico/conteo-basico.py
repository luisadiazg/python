print("\nWhile controlado con Conteo")
print("===========================\n")

print("Un ejemplo es un sumador numérico hasta 10, \ncomo se muestra a continuación:\n")

suma = 0;
numero = 1;
while numero <= 10:
    print("el numero a sumar es : ",numero);
    suma = numero + suma;
    print("el resultado parcial de la suma es : ",suma);
    numero = numero + 1;
print ("La suma total " + str(suma))

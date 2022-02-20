def fibonacci(num):
    if num in {0, 1}:  # sistema base
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)  # sistema recursivo

numero = int(input("Ingrese la cantidad numerica que componen Fibonacci :  "))
[fibonacci(num) for num in range(numero)]

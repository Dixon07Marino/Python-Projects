arreglo_numeros = []

def recibirNumero(numero):
    for num in range(1, numero+1):
        if num % 3 == 0 and num % 5 == 0:
            arreglo_numeros.append("FizzBuzz")
        elif num % 3 == 0:
            arreglo_numeros.append("Fizz")
        elif num % 5 == 0:
            arreglo_numeros.append("Buzz")
        else:
            arreglo_numeros.append(num)
    return arreglo_numeros

print(recibirNumero(15))

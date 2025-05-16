def sumar(num):
    return num + 1

numeros = [1, 2, 3, 4, 5]

resultado = map(sumar, numeros)

print(list(resultado))

#Con lambda

resultado = list(map(lambda num: num * 2, numeros))
print(resultado)

num_1 = [2, 3, 4, 7, 8]
num_2 = [5, 9, 33, 6, 2]

resultado = map(lambda num1, num2: num1 * num2, num_1, num_2)

print(tuple(resultado))


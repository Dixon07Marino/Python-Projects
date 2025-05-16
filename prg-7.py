#Recursividad - Encontrar factorial de 6

def encontrarFactorial(num):
    if num < 1:
        resultado = 1
    else:
        resultado = num * encontrarFactorial(num - 1)
    return resultado

print(f"El factorial de 6 es: {encontrarFactorial(6)}")
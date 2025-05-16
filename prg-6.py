#Generar contraseñas aleatorias

import string, random

def makePasswd(length=12):
    long_str = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(long_str) for _ in range(length))

while True:
    print("¡Bienvenido al generador de contraseñas!")
    length = int(input("Por favor, coloca la longitud de la contraseña: "))
    print(f"Tu contraseña es:\n{makePasswd(length)}")
    break
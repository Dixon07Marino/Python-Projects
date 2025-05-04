import random, string

while True:
    caracteres = string.ascii_letters
    print("Bienvenido al generador de contraseñas 🔒")
    longitud = int(input("Longitud deseada:"))
    opcion1 = input("¿Incluir números? (s/n):")
    opcion2 = input("¿Incluir símbolos? (s/n):")
    if opcion1 == "s" and opcion2 == "s":
        caracteres = string.ascii_letters + string.digits + string.punctuation
    elif opcion1 == "s":
        caracteres = string.ascii_letters + string.digits
    elif opcion2 == "s":
        caracteres = string.ascii_letters + string.punctuation
    else:
        caracteres = string.ascii_letters
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    print(f"Tu contraseña generada es: {password}")
    break
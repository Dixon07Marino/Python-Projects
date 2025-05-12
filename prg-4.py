#La sucesión de fibonacci

a, b = 0, 1

while a < 100:
    print(a)
    fib = a + b
    a = b
    b = fib
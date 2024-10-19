# Ejercicios propuestos - Core
# Basico
for i in range(101):
    print(i)

# Multiples de 2
for i in range(2, 501, 2):
    print(i)

# Contando Vanilla Ice
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# Wow. Número gigante a la vista
suma = 0
for i in range(0, 500001, 2):
    suma += i
print("Suma total de los números pares:", suma)

# Regrésame al 3
for i in range(2024, 0, -3):
    print(i)

# Contador dinámico
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)

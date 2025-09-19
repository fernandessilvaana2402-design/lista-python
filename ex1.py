contagem_pares = 0
contagem_impar = 0

for i in range (10):
    numero = int(imput(f"por fvor insira o{i + 1}numro inteio: "))
    if numero % 2 == 0:
        contagem_pares += 1
    else:
        contagem_impar += 1


print("total de numeros pares {contagem_pares}")
print("total de numeros impares {vontagem_impar}")
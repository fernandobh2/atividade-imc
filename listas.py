
import statistics
import random

def calcula_imc(peso=70, altura=1.75):
    return peso / (altura ** 2)

alturas = [45, 23, 67, 12, 11, 89, 23, 41, 50, 62, 78, 34, 56, 19, 72, 88, 11, 90, 39, 65,
           76, 27, 48, 59, 81, 14, 11, 93, 3, 68, 29, 52, 74, 16, 85, 20, 55, 38, 69, 11,
           83, 7, 44, 61, 18, 96, 22, 58, 31, 71, 40, 53, 87, 31]

print("Maior valor:", max(alturas))
print("Menor valor:", min(alturas))
print("Soma total:", sum(alturas))
print("Valor absoluto de -25:", abs(-25))
print("Arredondamento de 3.14159 para 2 casas decimais:", round(3.14159, 2))

print("Média:", statistics.mean(alturas))
print("Mediana:", statistics.median(alturas))
print("Moda:", statistics.mode(alturas))
print("Variância da amostra:", statistics.variance(alturas))
print("Desvio padrão da amostra:", statistics.stdev(alturas))

matriz_float = [[random.random() for _ in range(10)] for _ in range(5)]
matriz_int = [[random.randint(0, 9) for _ in range(4)] for _ in range(8)]

print("Matriz 5x10 de floats:")
for linha in matriz_float:
    print(linha)

print("Matriz 8x4 de inteiros:")
for linha in matriz_int:
    print(linha)

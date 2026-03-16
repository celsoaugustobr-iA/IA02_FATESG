import numpy as np

print("--- Exercício 1 ---")
# Crie um array de 10 elementos.
arr1 = np.arange(10)
print("Original:", arr1)
# Altere os valores de todos os elementos com índices de 5 a 8 para 0.
# Considerando índices 5, 6, 7 e 8 (inclusive)
arr1[5:9] = 0
print("Alterado:", arr1)

print("\n--- Exercício 2 ---")
# Crie um array com 3 linhas e 2 colunas.
arr2 = np.arange(6).reshape(3, 2)
print("Matriz:\n", arr2)
# Imprima o shape
print("Shape:", arr2.shape)
# Imprima a 2ª linha (índice 1)
print("2ª linha:", arr2[1])

print("\n--- Exercício 3 ---")
# Crie um array com 3 linhas e 2 colunas.
arr3 = np.arange(6).reshape(3, 2)
print("Matriz:\n", arr3)
# Imprima a 2ª coluna (índice 1)
print("2ª coluna:\n", arr3[:, 1])

print("\n--- Exercício 4 ---")
# Crie um array de com 4 linhas e 5 colunas.
arr4 = np.arange(20).reshape(4, 5)
print("Matriz:\n", arr4)
# Imprima os elementos da terceira linha (índice 2)
print("Elementos da 3ª linha:", arr4[2])

print("\n--- Exercício 5 ---")
# Crie um array de com 4 linhas e 5 colunas.
arr5 = np.arange(20).reshape(4, 5)
print("Matriz:\n", arr5)
# Imprima todos os elementos da primeira e segunda linhas (índices 0 e 1 -> 0:2)
# e segunda a terceira colunas (índices 1 e 2 -> 1:3).
print("Elementos (linhas 1-2, colunas 2-3):\n", arr5[0:2, 1:3])

print("\n--- Exercício 6 ---")
# Crie um array de com 4 linhas e 5 colunas.
arr6 = np.arange(20).reshape(4, 5)
print("Matriz:\n", arr6)
# Imprima todos os elementos da segunda e terceira linhas (índices 1 e 2 -> 1:3)
# e primeira a terceira colunas (índices 0, 1 e 2 -> 0:3).
print("Elementos (linhas 2-3, colunas 1-3):\n", arr6[1:3, 0:3])

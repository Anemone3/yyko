"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge2.kt
"""

r = [0] * 50


for n in range(50):
    if n in [0, 1]:
        r[0] = 0
        r[1] = 1
    else:
        r[n] = r[n - 1] + r[n - 2]
    print(r[n])

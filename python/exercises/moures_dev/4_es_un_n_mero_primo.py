"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge3.kt
"""

is_prim = lambda x: x % 2 != 0

r = [n for n in range(1, 101) if is_prim(n)]

print(r)

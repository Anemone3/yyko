"""
Escribe una función que calcule y retorne el factorial de un número dado
de forma recursiva.


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge13.kt
"""


def factorial_n(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial_n(number=number - 1)


print(factorial_n(10))

"""
Crea un programa se encargue de transformar un número
decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge8.kt
"""


def get_bin(number: int | float) -> str:
    n = number // 1
    d = number - n
    bin_n = []
    while n > 0:
        r = n % 2
        if r == 0:
            bin_n.append("0")
        else:
            bin_n.append("1")
        n = n // 2
    bin_n.reverse()
    bin_d = []
    for _ in range(10):
        d *= 2
        if d >= 1:
            bin_d.append("1")
            d -= 1
        else:
            bin_d.append("0")
    return "".join(bin_n) + "." + "".join(bin_d)

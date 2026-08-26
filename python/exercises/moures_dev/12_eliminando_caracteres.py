"""
Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO
estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO
estén presentes en str1.


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge11.kt
"""


def del_chars(str1: str, str2: str) -> dict[str, str]:
    out1 = ""
    out2 = ""

    for i in str1:
        if i not in str2:
            out1 += i

    for i in str2:
        if i not in str1:
            out2 += i

    return {"out1": out1, "out2": out2}


print(del_chars("casa", "manzana"))

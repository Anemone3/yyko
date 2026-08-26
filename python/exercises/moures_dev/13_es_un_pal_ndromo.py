"""
Escribe una función que reciba un texto y retorne verdadero o
falso (Boolean) según sean o no palíndromos.
Un Palíndromo es una palabra o expresión que es igual si se lee
de izquierda a derecha que de derecha a izquierda.
NO se tienen en cuenta los espacios, signos de puntuación y tildes.
Ejemplo: Ana lleva al oso la avellana.


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge12.kt
"""


def is_palindromo(text: str) -> bool:
    f_text = text.strip()
    left = 0
    right = len(f_text) - 1
    while True:
        if f_text[left] != f_text[right]:
            break
        left += 1
        right -= 1
    return False


test = "Ana lleva al oso la avellana"
print(test)
print("is palindromo: ", is_palindromo(test))

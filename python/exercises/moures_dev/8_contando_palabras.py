"""
Crea un programa que cuente cuantas veces se repite cada palabra
y que muestre el recuento final de todas ellas.
- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que
lo resuelvan automáticamente.


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge7.kt
"""


def count_words(text: str) -> dict:
    word_count = {}
    words = text.strip().split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

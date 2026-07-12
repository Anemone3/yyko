"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge1.kt
"""

s = "arca"
t = "cara"


def anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    char1 = sorted(word1)
    char2 = sorted(word2)
    print("1", char1)
    print("2", char2)

    return char1 == char2


r = anagram(s, t)
print("result ", r)

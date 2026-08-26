"""
Crea un programa que comprueba si los paréntesis, llaves y corchetes
de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cieran
en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios.
No hay uno más importante que otro.
- Expresión balanceada: { [ a * ( c + d ) ] - 5 }
- Expresión no balanceada: { a * ( c + d ) ] - 5 }


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge10.kt
"""

word = "{ [ a * ( c + d ) ] - 5 }"
word_2 = "{ a * ( c + d ) ] - 5 }"


def test(word: str) -> bool:
    corchetes = ["{", "}", "[", "]", "(", ")"]
    valid = []
    for w in word:
        if w in corchetes:
            if w not in valid:
                valid.append(w)
            else:
                valid.pop()

    return len(valid) % 2 == 0


if test(word=word) and (test(word=word_2) == False):
    print("Pass")

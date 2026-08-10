"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge6.kt
"""


def reverse_word(text: str) -> str:
    size = len(text)
    result = []
    while len(result) != len(text):
        result.append(text[size - 1])
        size -= 1
    return "".join(result)

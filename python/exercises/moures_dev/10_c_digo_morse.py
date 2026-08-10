"""
Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
- Debe detectar automáticamente de qué tipo se trata y realizar
la conversión.
- En morse se soporta raya "—", punto ".", un espacio " " entre letras
o símbolos y dos espacios entre palabras "  ".
- El alfabeto morse soportado será el mostrado en
https://es.wikipedia.org/wiki/Código_morse.


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge9.kt
"""

morse_map = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def parse_morse(text: str) -> str:
    result = ""
    for char in text:
        if char.upper() in morse_map:
            result += morse_map[char.upper()]
            result += " "
        else:
            result += " "
    return result

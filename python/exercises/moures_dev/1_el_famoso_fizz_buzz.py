"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge0.kt
"""

for n in range(1, 101):
    m_3 = n % 3 == 0
    m_5 = n % 5 == 0
    if m_3 and m_5:
        print("fizzbuzz")
    elif m_3:
        print("fizz")
    elif m_5:
        print("buzz")
    else:
        print(n)

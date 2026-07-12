"""
    Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
    de un lugar ficticio al pasar un número concreto de días según estas reglas:
    - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
    - Cada día que pasa:
    - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
    - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
    siguiente aumenta en un 20%.
    - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
    siguiente disminuya en un 20%.
    - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
    - La función recibe el número de días de la predicción y muestra la temperatura
    y si llueve durante todos esos días.
    - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.


    Solución:
    https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%2343%20-%20SIMULADOR%20DE%20CLIMA%20%5BF%C3%A1cil%5D/ejercicio.md
"""



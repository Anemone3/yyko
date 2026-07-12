"""
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.


Solución:
https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge4.kt
"""

from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Triangulo(Polygon):
    def __init__(self, b, h) -> None:
        self.base = b
        self.height = h

    def area(self) -> float:
        return (self.base * self.height) / 2


class Cuadrado(Polygon):
    def __init__(self, lado) -> None:
        self.lado = lado

    def area(self) -> float:
        return self.lado * self.lado


class Rectangulo(Polygon):
    def __init__(self, b, h) -> None:
        self.base = b
        self.height = h

    def area(self) -> float:
        return self.height * self.base


def calc_poligono(poligono: Polygon):
    return poligono.area()


print(calc_poligono(Triangulo(10, 5)))
print(calc_poligono(Rectangulo(10, 5)))
print(calc_poligono(Cuadrado(4)))

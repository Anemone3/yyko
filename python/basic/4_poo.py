from abc import ABC, abstractmethod
from dataclasses import dataclass


class Habilidades(ABC):
    @abstractmethod
    def correr(self, uma: Uma) -> float:
        pass


@dataclass
class Stats:
    velocidad: float
    stamina: float
    power: float
    guts: float
    wisdom: float


class Uma:
    def __init__(self, nombre: str, stats: Stats, habilidad: Habilidades):
        self.nombre = nombre
        self.stats = stats
        self.habilidad = habilidad

    def correr(self):
        return self.habilidad.correr(self)


class Runner(Habilidades):
    def correr(self, uma: Uma) -> float:
        return uma.stats.velocidad * 1.2


class Leader(Habilidades):
    def correr(self, uma: Uma) -> float:
        return uma.stats.velocidad + (uma.stats.stamina * 0.3)


class Chaser(Habilidades):
    def correr(self, uma: Uma) -> float:
        return uma.stats.velocidad * 0.8 + uma.stats.power * 0.5


uma1 = Uma("Special Week", Stats(900, 800, 700, 600, 650), Runner())
uma2 = Uma("Gold Ship", Stats(850, 900, 750, 700, 600), Chaser())

print(f"{uma1.nombre} corrio: ", uma1.correr())
print(f"{uma2.nombre} corrio: ", uma2.correr())

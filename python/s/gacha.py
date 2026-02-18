import random
import numpy as np
import time


random.seed() # Mersenne Twister como c++ pero python lo usa por defecto
rng = np.random.default_rng() # similar usando numpy


class Character:
    name:str
    star:int

    characters_5 = ["Furina", "Varesa", "Hu tao", "Miyabi"]
    characters_4 = ["Nekomata", "Barbara", "Yuzuha", "Alice", "Shun gua"]


    def __init__(self, name=None, star=None):
        self.name = name
        self.star = star

    def __str__(self):
        return f"{self.name} ({self.star})" 

    def __repr__(self):
        return f"{{'{self.name}', {self.star}}}"

    def get_character(self, star):
        if star == 5:
            return list(map(lambda x: Character(x, 5), self.characters_5))
        elif star == 4:
            return list(map(lambda x: Character(x, 4), self.characters_4))
        else:
            return []


    def get_character_by_name(self, name):
        if name in self.characters_5:
            return Character(name, 5)
        elif name in self.characters_4:
            return Character(name, 4)
        else:
            return None


items_gacha = [
    # Genshin Impact (armas 4★)
    "Favonius Sword", "Sacrificial Bow", "The Widsith", "Dragon's Bane",
    "Favonius Lance", "Rust", "The Stringless",
    # Zenless Zone Zero (W-Engines)
    "Starlight Engine", "Demara Battery", "Steel Cushion", "Cannon Rotor",
    "Electro-Lip Gloss", "Slice of Time",
    # Honkai: Star Rail (Light Cones 4★)
    "Post-Op Conversation", "Dance! Dance! Dance!", "Memories of the Past",
    "The Moles Welcome You", "Subscribe for More!", "Landau's Choice", "Woof! Walk Time!"
]



def main():
    character = Character()
    v_character5 = character.get_character(5)
    v_character4 = character.get_character(4)
    v_items = items_gacha

    inventory = []

    MAX_PITTY = 90
    MIN_PITTY = 65

    CHANCE_5_STAR = 0.6
    CHANCE_4_STAR = 5.7


    opt, count_wish, pitty_v = 0, 0, [90]

    is_start = True

    while is_start:

        can_press_key = True

        print("""
        1.- Tirar 10 deseos
        2.- Tirar 1 deseo
        3.- Mostrar deseos
        4.- Salir
        """)

        
        opt = int(input("Elige una opcion: "))

        roll = rng.uniform(0, 100)
        prob_n = 70 + (roll / 100) * (MAX_PITTY - MIN_PITTY)
        pitty_v.append(prob_n)
        match opt:
            case 1:
                print("Tirar 10 deseos")

                received_4_star = False

                pitty_prob = rng.choice(pitty_v)
                print("pitty prob ", pitty_prob)
                for i in range(10):
                    roll = rng.uniform(0, 100)
                    count_wish += 1
                    print(f"wish {count_wish}", end="", flush=True)
                    for _ in range(2): time.sleep(1); print(".", end="", flush=True)
                    print()
                    print("roll", roll)
                    if roll < CHANCE_5_STAR:
                        character = rng.choice(v_character5)
                        inventory.append(character)
                        print(f"⭐⭐⭐⭐⭐ {character.name}")
                        continue
                    elif received_4_star == False:
                        received_4_star = True
                        character = rng.choice(v_character4)
                        inventory.append(character)
                        print(f"⭐⭐⭐⭐ {character.name}")
                        continue
                    elif count_wish == MAX_PITTY or count_wish == int(pitty_prob) or count_wish == int(prob_n):
                        character = rng.choice(v_character5)
                        inventory.append(character)
                        print(f"⭐⭐⭐⭐⭐ {character.name}")
                        continue
                    elif roll < CHANCE_5_STAR + CHANCE_4_STAR:
                        character = rng.choice(v_character4)
                        inventory.append(character)
                        print(f"{'⭐' * character.star} {character.name}")
                        continue
                    else:
                        item = rng.choice(v_items)
                        print(f"⭐⭐⭐ {item}")
                        
            case 2:
                print("Tirar 1 deseo")
            case 3: 
                for character in inventory:
                    print(f"{'⭐' * character.star} {character.name}")
            case 4:
                print("Salir")
                is_start = False
            case _:
                print("Opcion no valida")
   
    return 0









if __name__ == "__main__":
    main()
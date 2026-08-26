ventas = [
    ("Laptop", 2),
    ("Mouse", 5),
    ("Laptop", 3),
    ("Teclado", 1),
    ("Mouse", 2),
    ("Monitor", 4),
    ("Laptop", 1),
]

ob: dict[str, int] = {}

for product, cantidad in ventas:
    ob[product] = ob.get(product, 0) + cantidad

print(ob)

###

logs = [
    "juan",
    "maria",
    "juan",
    "pedro",
    "maria",
    "ana",
    "juan",
]

no_repet = set(logs)
print(no_repet)


###

jugadores = [
    ("Luis", 340),
    ("Ana", 500),
    ("Pedro", 120),
    ("Juan", 430),
]

result = []
while len(result) != len(jugadores):
    max_score = 0
    index = 0
    for idx, player in enumerate(jugadores):
        _, score = player
        if max_score < score and player not in result:
            max_score = score
            index = idx
    result.append(jugadores[index])

print(result)

"""
Sin result ->
"""
n = len(jugadores)

for i in range(n):
    for j in range(n - 1 - i):
        _, score1 = jugadores[j]
        _, score2 = jugadores[j + 1]

        if score1 < score2:
            jugadores[j] = jugadores[j + 1]
            jugadores[j + 1] = jugadores[j]
print(jugadores)


##

juan = {
    "Ana",
    "Pedro",
    "Luis",
    "Maria",
}

maria = {
    "Pedro",
    "Carlos",
    "Ana",
}
s_t = juan.intersection(maria)
s_t = juan & maria

###
history_search = [
    ("VISIT", "google.com"),
    ("VISIT", "github.com"),
    ("VISIT", "stackoverflow.com"),
    ("BACK",),
    ("BACK",),
    ("VISIT", "python.org"),
]

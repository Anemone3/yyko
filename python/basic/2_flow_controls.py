# clasico if
koyori = False
result_if = ""
if koyori:
    result_if = "if"
elif koyori != True:
    result_if = "elif"
else:
    result_if = "else koyori"

print("result if: ", result_if)

# Match - case  (switch)

type = "text"
result_match = ""
match type:
    case "text":
        result_match = "are you seeing a text"
    case "image":
        result_match = "are you seeing a image"
    case _:
        result_match = "whatever"

print("result match: ", result_match)


# bucles and tools como ["break", "continue","pass"]

# for
nums = [1, 2, 3, 4]
MAX_LIMIT = 100
result_for_and_tools = []
for n in nums:

    nums.append(n + 1)
    pass

    result_for_and_tools.append("pass")
    # print(nums)
    # print(n)
    if 4 == n:
        result_for_and_tools.append("continue")
        nums = [0] * MAX_LIMIT
        continue

    if len(nums) >= MAX_LIMIT:
        result_for_and_tools.append("break")
        break

print("result for and tools['break','continue','pass']: ", result_for_and_tools)


# while
counter = 0
less_counter = 0
result_while = []
while counter < 10:
    # print(counter)
    result_while.append(counter)
    if less_counter == -3:
        result_while.append("break")
        break
    if counter <= 3:
        counter += 1
        result_while.append("continue")
        continue

    less_counter -= 1


print("result while: ", result_while)


# with
# se necesita tener un proceso, tambien hay manera usando @context_manager para funciones
class Process:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print(f"--[INICIO] Preparando proceso: {self.nombre}")
        return self  # esto se asigna al as

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            import traceback

            print("--- REPORTE DE ACCIDENTE ---")
            # Extraemos la información del objeto exc_tb
            detalles = traceback.format_tb(exc_tb)
            print(f"Mensaje: {exc_val}")
            print(f"Tipo: {exc_type.__name__}")
            print(
                f"Línea del error: {detalles[-1].strip()}"
            )  # La última línea del rastro

            # Aquí podrías guardar 'detalles' en un archivo .log
            return False  # Deja que el programa falle después de avisar,
            # o True para que el restso del codigo siga
        print(f"--[FIN] Limpiando y cerrando el proceso: {self.nombre}")


# usando with
print("result with:")
with Process("some_process") as proceso:
    # force_error = 10 / 0
    print("Ejecutando proceso: ", proceso)


# crear listas mediante un for condition
my_list = [value for value in range(10) if value % 2 == 0]
print("result list by for condition: ", my_list)


# yield
def store():
    yield "chocolac"
    yield "dulces"
    yield "non biyori"
    return "opening the store"


gen = store()
print(next(gen))
print(next(gen))
print(next(gen))


def other_store():
    mensaje = yield from store()
    print(f"Mensaje recibido de otra funcion con yield: ", mensaje)
    return "New Game"


# gen = store()
# while True:
#     try:
#         item = next(gen)
#         print(f"Recibido: {item}")
#     except StopIteration as e:
#         print(f"El generador dijo: {e.value}")  # Aquí aparece el "opening store"
#         break

for x in other_store():
    print(x)


# asignacion normal
text = "ariku"
range = len(text)
if range > 5:
    print(f"result usando =")
# asignacion corta, asignarlo a una variable en una estructura flow
if (rango := len(text)) > 5:
    print(f"result usando := ")


def calcular_impuesto(val):
    return val * 0.18


precios = [100, 250, 400]

# Calculamos, guardamos en 'i' y lo usamos para filtrar y para la lista final
facturas = [i for p in precios if (i := calcular_impuesto(p)) > 50]
print("facturas: ", facturas)

# sin :=
# Se calcula una vez para el 'if' y otra vez para la lista
facturas = [calcular_impuesto(p) for p in precios if calcular_impuesto(p) > 50]
print("facturas: ", facturas)


datos = {"radio": (r := 10), "circunferencia": 2 * 3.14 * r, "area": 3.14 * (r**2)}

print("datos usando := \n",datos)
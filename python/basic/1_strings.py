ariku = "  ariku  " # Le agregamos espacios para probar los métodos de limpieza

# 1. Transformaciones
print("--- TRANSFORMACIONES ---")
print(f"Original con espacios: '{ariku}'")
print(f"Mayúsculas:            '{ariku.upper().strip()}'")
print(f"Título:                '{ariku.title().strip()}'")
print(f"Intercambio:           '{ariku.swapcase().strip()}'")

# 2. Limpieza (Strip)
print("\n--- LIMPIEZA ---")
print(f"Sin espacios:          '{ariku.strip()}'")
print(f"Sin espacios izq:      '{ariku.lstrip()}'")

# 3. Búsqueda y Reemplazo
# Usamos .strip() primero para que la búsqueda sea exacta
limpio = ariku.strip() 
print("\n--- BÚSQUEDA Y REEMPLAZO ---")
print(f"¿Empieza con 'a'?:     {limpio.startswith('a')}")
print(f"¿Termina con 'u'?:     {limpio.endswith('u')}")
print(f"Cambiar 'k' por 'qu':  {limpio.replace('k', 'qu')}")
print(f"Contar letras 'a':     {limpio.count('a')}")

# 4. Validaciones
print("\n--- VALIDACIONES ---")
print(f"¿Es solo texto?:       {limpio.isalpha()}")
print(f"¿Es un número?:        {limpio.isdigit()}")

# 5. División y Unión
print("\n--- DIVISIÓN Y UNIÓN ---")
palabras = "python,java,javascript".split(",")
print(f"Lista creada:          {palabras}")
print(f"Unido por guiones:     {'-'.join(palabras)}")

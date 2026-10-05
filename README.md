
* Atajo de java para crear file:
    - cjava

## Ejecutar archivos

### Python (LeetCode)
```bash
# El lenguaje es Python por defecto
python test.py contains_duplicates "[1, 2, 3, 3]"
python test.py is_anagram rat car

# Tambien se puede indicar explicitamente para extender el runner a otros lenguajes
python test.py --language python contains_duplicates "[1, 2, 3, 3]"
```

### C++
```bash
# Solo ver resultado (no guarda binario)
g++ -std=c++17 archivo.cpp && ./a.out

# Guardar binario con nombre propio
g++ -std=c++17 -o salida archivo.cpp && ./salida

# Clang (alternativa)
clang++ -std=c++17 archivo.cpp && ./a.out
```

### Java
```bash
# Ejecutar directo (sin compilar)
java Archivo.java
```
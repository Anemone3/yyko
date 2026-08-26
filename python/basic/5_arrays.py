yko = [1, 2, 3, 4, 5, 6, 7]


r_yko = yko[::-1]

print("antes: ", yko)
print("despues: ", r_yko)

"""
Array slicing

[start:end:step]

-> [1,2,3,4,5,6,7,8]
-> [2::2] -> [3,5,7]
-> [4::-2] -> [5,3,1]
-> [-1::-2] -> [7,5,3,1]

"""


mtx = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
resultado = [fila[1:3] for fila in mtx[0:2]]
print(resultado)


import numpy as np

# DArray que viene de C

mtx_np = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(mtx_np[:, :2])  # no idea, practicarlo

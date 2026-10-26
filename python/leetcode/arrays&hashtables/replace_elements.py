class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        mayor = -1
        for i in range(len(arr) - 1, -1, -1):
            print("indice: ", i)
            print("n: ", arr[i])
            print("mayor: ", mayor)
            old_mayor = mayor
            if arr[i] > mayor:
                mayor = arr[i]
                print("mayor actual: ", mayor)
                print("indice actual: ", arr[i])
            arr[i] = old_mayor
            print("============")
        return arr

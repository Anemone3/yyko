class Nodo:
    value: any
    next_node: any

    def __init__(self, value):
        self.value = value
        self.next_node = None


class ListaEnlazada:
    head: Nodo

    def __init__(self, val: any):
        self.head = Nodo(val)

    def append(self, value):
        nuevo = Nodo(value)
        punt = self.head
        while punt.next_node is not None:
            punt = punt.next_node
        punt.next_node = nuevo

    def show(self):
        punt = self.head
        while punt is not None:
            print(punt.value, end=" -> ")
            punt = punt.next_node
        print("None")

    def find_value(self, value):
        punt = self.head
        bucles = 0
        while punt is not None:
            if punt.value == value:
                return bucles
            punt = punt.next_node
            bucles += 1

        return -1


def main():
    list = ListaEnlazada(10)
    list.append(10)
    list.append(13)

    list.show()



if __name__ == "__main__":
    main()

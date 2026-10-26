class User:
    def __init__(self) -> None:
        self.rank = -8
        self.progress = 0

    def inc_progress(self, val):
        if val not in [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7]:
            raise ValueError("Sobrepasa el valor cambio")

        

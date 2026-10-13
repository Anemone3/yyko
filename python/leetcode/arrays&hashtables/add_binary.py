class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def sum(q, w):
            if q == "0" and w == "0":
                return ["0", "0"]
            if q == "1" and w == "1":
                return ["1", "0"]
            return ["0", "1"]

        if len(a) < len(b):
            a = ("0" * (len(b) - len(a))) + a
        elif len(b) < len(a):
            b = ("0" * (len(a) - len(b))) + b

        i = len(a) - 1
        binary = ""
        res = "0"
        while i >= 0:
            carry_1, x = sum(a[i], b[i])
            carry_2, x = sum(x, res)
            res = "1" if carry_1 == "1" or carry_2 == "1" else "0"
            binary = x + binary
            i -= 1
        if res == "1":
            binary = res + binary

        return binary

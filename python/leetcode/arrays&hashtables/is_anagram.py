from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c_s = Counter(s)
        c_t = Counter(t)
        print("coutner s", c_s)
        print("counter t", c_t)
        for key, _ in c_s.items():
            if key not in c_t:
               return False
            if c_s[key] != c_t[key]:
                return False
        return True

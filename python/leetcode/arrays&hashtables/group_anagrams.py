class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ark: dict[str, list[str]] = {}
        for word in strs:
            w_order = str("".join(sorted(word)))
            if w_order in ark.keys():
                ark[w_order].append(word)
            else:
                ark[w_order] = [word]

        # result = []
        # for v in ark.values():
        #     result.append(v)
        # return result
        return list(ark.values())

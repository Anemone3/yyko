class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            if n in hash_map:
                return [hash_map[n], i]
            
            val = target - n
            hash_map[val] = i

        return []

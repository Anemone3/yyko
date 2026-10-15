"""
1929. Concatenation of Array
https://leetcode.com/problems/concatenation-of-array/description
"""


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, s in enumerate(nums):
            ans[i] = s
            ans[i + n] = s

        return ans

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        koyo = len(nums)
        answer = [0] * koyo
        post_fix, answer[0] = 1, 1

        for n in range(1, koyo):
            answer[n] = nums[n - 1] * answer[n - 1]

        for n in reversed(range(koyo)):
            answer[n] *= post_fix
            post_fix *= nums[n]
        return answer

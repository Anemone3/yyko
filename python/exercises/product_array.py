def productExceptSelf(nums: list[int]) -> list[int]:
    output = []
    for i in range(len(nums)):
        result = mult(nums[i - 1::])
        output.append(result)
    pass


def mult(nums):
    res = 1
    for n in nums:
        res *= n
    return res


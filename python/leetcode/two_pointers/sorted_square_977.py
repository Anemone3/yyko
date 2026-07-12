nums = [-4, -1, 0, 3, 10]
expect = [0, 1, 9, 16, 100]


l = 0
r = len(nums) - 1

result: list[int] = [0] * len(nums)
while l <= r:
    x = nums[l] * nums[l]
    y = nums[r] * nums[r]
    print(f"left [{x}] | right [{y}]")

    if x > y:
        result[r - l] = x
        l += 1
    else:
        result[r - l] = y
        r -= 1

    print(f"x: {l} |  y: {r}")

print(result)

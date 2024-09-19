nums = sorted([int(num) for num in input().split()])

a, b, c = nums[0], nums[1], nums[2]

if c == a + b:
    c = nums[3]

print(a, b, c)
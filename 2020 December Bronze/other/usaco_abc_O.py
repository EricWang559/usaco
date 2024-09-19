import sys
input = sys.stdin.read
nums = list(map(int, input().split()))
a, b, c, d = sorted(nums)[:4]  # Sort and select only the first 4 elements
sys.stdout.write(f"{a} {b} {d}\n" if c == a + b else f"{a} {b} {c}\n")

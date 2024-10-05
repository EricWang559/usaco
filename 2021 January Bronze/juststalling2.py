input()
A, B, count = sorted([int(i) for i in input().split()])[::-1], [int(j) for j in input().split()], 1
for c in range(len(A)):
    temp = 0
    for h in range(len(B)):
        if A[c] <= B[h]:temp+=1
    count *= (temp - c)
print(count)
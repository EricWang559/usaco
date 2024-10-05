N = input()
A = [int(i) for i in input().split()]
B = [int(j) for j in input().split()]

def prob(cows, heights):
    count = 1
    cows = sorted(cows)[::-1]

    for c in range(len(cows)):
        temp = 0
        for h in range(len(heights)):
            #print(f'h = {h}')
            if cows[c] <= heights[h]:
                temp+=1
                #print('t++')
        #print(f'temp = {temp}, count = {count}\n')
        count *= (temp - c)
        #print(f'count = {count}')

    print(count)
prob(A,B)



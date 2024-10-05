cycle = enumerate(['Ox','Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat'])
N = input()

diffB = 0

for i in range(N):
    line = [str(s) for s in input.split()]
    if line[3] == 'previous':
        #minus
        diffB-=cycle[line[4]]
        pass
    elif line[3] == 'next':
        #add
        pass  
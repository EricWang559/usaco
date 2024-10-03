def cycles(ab, w):
    count = 0
    i = 0
    while i < len(w):
        for j in range(0, len(ab)):
            if w[i] == ab[j]:
                #print(f'match at i:{i} for {w[i]} and j:{j} for {ab[j]}')
                i+=1
                if(i == len(w)):
                    break
        #print(f'count increase at {i} loop')
        count+=1
    return count

cowphabet = list(str(input()))
word = input()

'''
abcdefghijklmnopqrstvwxyz
mood
'''
print(cycles(cowphabet, word))



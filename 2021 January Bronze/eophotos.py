N = input()
arr = [int(inp) for inp in input().split()]

def eotos(num, ar):
    even, odd = 0, 0

    for i in arr:
        if i % 2 == 0:
            even+=1
        else:
            odd+=1
    
    #print(f'odd: {odd}')
    #print(f'even: {even}')

    singles = (max(odd, even) - abs(odd - even))


    if(odd > even):
        odd -= singles
        even = 0 #only odd
    elif(even > odd):
        even -= singles
        odd = 0 #only even
    
    start = '' 

    if singles % 2 == 0:
        start = 'even'
    elif singles % 2 == 1:
        start = 'odd'

    #print(f'{2*singles} grouped in singles already')
    #print(f'starting on {start} grouping')

    count = 2*singles

    if start == 'even':
        if not even:
            while odd > 0:
                if odd >=2:
                    odd -= 2
                    count+=1
                    #print(f'EVEN GROUP (-2 odd)\n odd = {odd}, count = {count}')
                else:
                    return count
                if odd >= 3:
                    odd -=1
                    count+=1
                    #print(f'ODD GROUP >3 (-1 odd)\n odd = {odd}, count = {count}')
                elif odd >= 2:
                    odd -=2
                    #print(f'Even group >2 (-2 odd)\n odd = {odd}, count = {count}')
                else:
                    return count

        if not odd:
            while even > 0:
                if even >= 1:
                    even -=1
                    count+=1
                    #print(f'even = {even}, count = {count}')
                else:
                    return count
                return count
    elif start == 'odd':
        if not even:
            while odd > 0:
                if odd >= 3:
                    odd -=1
                    count+=1
                    #print(f'ODD GROUP >3 (-1 odd)\n odd = {odd}, count = {count}')
                elif odd >= 2:
                    odd -=2
                    count+=1
                    #print(f'Even group >2 (-2 odd)\n odd = {odd}, count = {count}')
                else:
                    return count - 1
                if odd >=2:
                    odd -= 2
                    count+=1
                    #print(f'EVEN GROUP >2 \nodd = {odd}, count = {count}')
                else:
                    return count
        elif not odd:
            return count + 1
    return count

print(eotos(N, arr))
N = input()
arr = [int(inp) for inp in input().split()]

def eophotos(num, arr):
    even, odd = 0, 0

    for i in arr:
        if i % 2 == 0:
            even+=1
        else:
            odd+=1


    groups = 0
    if(even != 0 and odd != 0):
        groups = abs(even - odd)
        
    if groups % 2 == 1: #ODD FIRST
        if(even>odd):
            even-=odd
            while(even > 0):
                #ODD CASE
                even-=3
                groups+=1
                print(f'groups increased')

                #EVEN CASE
                if(even == 0):
                    break
                even-=1
                groups+=1
                print(f'groups increased')

        else:
            odd-=even
            while(odd > 0):
                #ODD CASE
                if odd >=1:
                    odd-=1
                    groups+=1
                    print(f'groups increased, odd {odd}')

                #EVEN CASE
                if odd >=2:
                    odd-=2
                    groups+=1
                    print(f'groups increased, even {odd}')

    else:  #EVEN FIRST
        if(even>odd):
            even-=odd
            while(even > 0):
                #EVEN CASE
                if even >= 1:
                    even-=1
                    groups+=1
                    print(f'groups increased, even')

                #ODD CASE
                if even >= 3:
                    even-=3
                    groups+=1
                    print(f'groups increased, odd')
            
        else:
            odd-=even
            while(odd > 0):
                #EVEN CASE
                odd-=2
                groups+=1
                print(f'groups increased')

                #ODD CASE
                if(odd == 0):
                    break
                odd-=1
                groups+=1
                print(f'groups increased')
    return groups

print(eophotos(N, arr))
N = input()
cows = input()

def photo(num, arr):
    count = 0

    for i in range(3, len(arr)+1):
        #print(f'i = {i}\n\n')
        
        start = 0

        end = start+i-1
        while(start < len(arr) - i + 1 and end < len(arr)):
            print(f'start = {start}, end = {end}')
            g = 0
            h = 0
            for j in range(start,end+1):
                print(f'j={arr[j]}:{j}')
                if arr[j] == 'G':
                    g+=1
                else:
                    h+=1
            print(f'g = {g}, h = {h}')
            start+=1
            end+=1

            if not(g == 1 or h ==1):
                count+=1
                print(f'count++, g{g},h{h}')
    print(count)
photo(N, cows)
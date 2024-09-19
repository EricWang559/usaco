def avg_flower(flowers, petals):
    count = 0

    # Iterate over all possible subarrays
    for i in range(flowers):
        tsum = 0
        for j in range(i, flowers):
            tsum += petals[j]
            length = j - i + 1
            # Check if the average is an integer
            if tsum % length == 0:
                average = tsum // length
                # Check if any flower in the subarray has the average number of petals
                if average in petals[i:j+1]:
                    count += 1
                    #print(f"Subarray ({i}, {j}): petals = {petals[i:j+1]}, average = {average}")

    return count

# Input reading
num_flowers = int(input())
num_petals = [int(petals) for petals in input().split()]

# Function call and output
result = avg_flower(num_flowers, num_petals)
print(result)

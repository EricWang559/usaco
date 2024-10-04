def max_groups(cows):
    # Count even and odd cows
    even_count = 0
    odd_count = 0
    
    for cow in cows:
        if cow % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Max possible groups is 2 * min(even_count, odd_count) + 1
    # If odd_count > even_count, we can start with an odd group and alternate
    # If even_count >= odd_count, we can start with an even group and alternate
    if odd_count > even_count:
        return 2 * even_count + 1
    else:
        return 2 * odd_count

# Input reading
N = int(input())  # Number of cows
cows = list(map(int, input().split()))  # Breed IDs of cows

# Output the maximum number of groups
print(max_groups(cows))

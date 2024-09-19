# Reading inputs
l1 = [int(n1) for n1 in input().split()]
n, m = l1[0], l1[1]

l2 = [int(n2) for n2 in input().split()]  # Initial heights of the cows
l3 = [int(n3) for n3 in input().split()]  # Heights of the candy canes
hlist = list()

def fcows(cow_heights, candy_heights):
    for cane_height in candy_heights:  # For each candy cane
        current_candy_height = cane_height  # Set the height of the current candy cane
        for ch in cow_heights:  # Loop through each cow

            if current_candy_height <= 0:  # If no candy is left, exit the loop
                break

            if ch >= current_candy_height:  # Cow can eat the whole remaining candy
                ch += current_candy_height  # Cow eats the candy
                current_candy_height = 0  # No candy left

            else:  # Cow can only eat up to its height
                temp1 = current_candy_height
                current_candy_height -= ch
                ch += (temp1 - current_candy_height)
            hlist.append(ch)

    # Output final heights of the cows
    for h in hlist:
        print(h)

fcows(l2, l3)
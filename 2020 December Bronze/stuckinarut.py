# Input number of cows
num_cows = int(input())

# Input the direction and coordinates for each cow
cow_data = [input().split() for cowcow in range(num_cows)]


def 人工(num_cows, cows):
    '''
    6
    E 3 5
    N 5 3
    E 4 6
    E 10 4
    N 11 2
    N 8 1
    '''
    cows_prime = []
    #for i in range(num_cows):
        #cows_prime[i] = list(cows[1], cows[2])

    Elist_x = [] #the changing one
    Elist_y = []
    Nlist_x = [] #the changing one
    Nlist_y = []

    for cow in cows:
        print(cow)
        if cow[0] == 'E':
            Elist_x.append(int(cow[1]))
            Elist_y.append(int(cow[2]))

        elif cow[0] == 'N':
            Nlist_x.append(int(cow[1]))
            Nlist_y.append(int(cow[2]))
        else:
            print('Invalid cow type')
        
    print('Elist:', Elist_x, Elist_y)
    print('Nlist:', Nlist_x, Nlist_y)

    dead_patches = []

    arr = []

    for i in range(num_cows):
        for e in range(Elist_x):
            dead_patches.append(Elist_x[e], Elist_y[e])
            Elist_x[e]+=1
        for n in range(Nlist_x):
            dead_patches.append(Nlist_x[e], Nlist_y[e])
            Nlist_x[e]+=1
        for i in range(cows_prime):
            if cows_prime[i] in dead_patches:
                print("COW STOPPED AT ", cows_prime[i])
                #not done yet, need to implemetn return 



def 人工智能(n,c):
    num_cows = n
    cows = c

    # Convert coordinates to integers
    for cow in cows:
        cow[1], cow[2] = int(cow[1]), int(cow[2])

    # List to store results for each cow
    results = ['Infinity'] * num_cows  # Default to Infinity

    # Keep track of grass patches eaten (x, y positions)
    eaten_grass = []

    # Simulation loop: we need to track each cow's movements and see if it stops
    for i in range(num_cows):
        # Get the current cow's details
        cow = cows[i]
        direction, x, y = cow[0], cow[1], cow[2]
        steps = 0

        while True:
            # If the cow has already eaten this patch of grass, stop
            if (x, y) in eaten_grass:
                results[i] = steps
                break
            
            # Eat the grass at the current position
            eaten_grass.append((x, y))
            steps += 1
            
            # Move the cow in the correct direction
            if direction == 'E':
                x += 1  # Move east
            elif direction == 'N':
                y += 1  # Move north
            
            # Check if the cow is still moving or needs to stop
            # (This is where the logic of stopping would be more complex)
            # If no other cow stops this cow, it will eventually move infinitely.

    # Output the results
    for result in results:
        print(result)

#人工智能(num_cows, cows)

def simulate_cows(num_cows, cow_data):
    # Initialize results and grass patches
    results = ['Infinity'] * num_cows  # Default to Infinity for all cows
    eaten_grass = {}  # Track which cows have eaten which grass patches

    # Split cows into east-moving and north-moving lists
    east_cows = []  # (x, y, cow_id)
    north_cows = []  # (x, y, cow_id)
    
    for i, cow in enumerate(cow_data):
        direction, x, y = cow[0], int(cow[1]), int(cow[2])
        if direction == 'E':
            east_cows.append((x, y, i))
        elif direction == 'N':
            north_cows.append((x, y, i))
    
    # Function to check if a cow should stop due to previously eaten grass
    def should_stop(x, y):
        if (x, y) in eaten_grass:
            return True
        return False
    
    # Simulate cow movements
    time = 0
    while east_cows or north_cows:
        # Track cells visited this time step
        current_cells = {}

        # Move east-moving cows
        for i, (ex, ey, e_id) in enumerate(east_cows):
            new_pos = (ex + 1, ey)
            if new_pos not in current_cells:
                current_cells[new_pos] = []
            current_cells[new_pos].append(('E', e_id))
            east_cows[i] = (new_pos[0], new_pos[1], e_id)
        
        # Move north-moving cows
        for i, (nx, ny, n_id) in enumerate(north_cows):
            new_pos = (nx, ny + 1)
            if new_pos not in current_cells:
                current_cells[new_pos] = []
            current_cells[new_pos].append(('N', n_id))
            north_cows[i] = (new_pos[0], new_pos[1], n_id)

        # Check the cells for cows that need to stop
        for cell, cows in current_cells.items():
            if len(cows) > 1:
                # Multiple cows are on the same cell, they share the cell
                for direction, cow_id in cows:
                    eaten_grass[cell] = eaten_grass.get(cell, []) + [cow_id]
            else:
                # Single cow on this cell
                direction, cow_id = cows[0]
                if should_stop(*cell):
                    results[cow_id] = time  # Record the time when the cow stops
                else:
                    eaten_grass[cell] = eaten_grass.get(cell, []) + [cow_id]

        # Check if there are any cows left that should be processed
        east_cows = [(x, y, i) for x, y, i in east_cows if results[i] == 'Infinity']
        north_cows = [(x, y, i) for x, y, i in north_cows if results[i] == 'Infinity']
        
        # Increment time step
        time += 1

    # Output the result for each cow
    for result in results:
        print(result)

# Call the function to simulate and print results
simulate_cows(num_cows, cow_data)

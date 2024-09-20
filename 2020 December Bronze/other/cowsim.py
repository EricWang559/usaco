def simulate_cows(num_cows, cow_data):
    from collections import defaultdict

    # Initialize results and grass patches
    results = ['Infinity'] * num_cows  # Default to Infinity for all cows
    eaten_grass = set()  # Track which cells have been eaten
    cow_positions = {}  # Track current positions of cows
    cow_directions = {}  # Track directions of cows
    
    east_cows = []  # (x, y, cow_id)
    north_cows = []  # (x, y, cow_id)
    
    for i, cow in enumerate(cow_data):
        direction, x, y = cow[0], int(cow[1]), int(cow[2])
        if direction == 'E':
            east_cows.append((x, y, i))
            cow_positions[i] = (x, y)
            cow_directions[i] = direction
        elif direction == 'N':
            north_cows.append((x, y, i))
            cow_positions[i] = (x, y)
            cow_directions[i] = direction

    # Simulation loop
    time = 0
    while east_cows or north_cows:
        current_cells = defaultdict(list)

        # Move east-moving cows
        for (ex, ey, e_id) in east_cows:
            new_pos = (ex + 1, ey)
            current_cells[new_pos].append(('E', e_id))
            cow_positions[e_id] = new_pos

        # Move north-moving cows
        for (nx, ny, n_id) in north_cows:
            new_pos = (nx, ny + 1)
            current_cells[new_pos].append(('N', n_id))
            cow_positions[n_id] = new_pos

        # Check the cells for cows that need to stop
        for cell, cows in current_cells.items():
            if len(cows) > 1:
                # Multiple cows are on the same cell, they share the cell
                for direction, cow_id in cows:
                    eaten_grass.add(cell)
            else:
                # Single cow on this cell
                direction, cow_id = cows[0]
                if cell in eaten_grass:
                    results[cow_id] = time  # Record the time when the cow stops
                else:
                    eaten_grass.add(cell)

        # Remove cows that have stopped
        east_cows = [(x, y, i) for (x, y, i) in east_cows if results[i] == 'Infinity']
        north_cows = [(x, y, i) for (x, y, i) in north_cows if results[i] == 'Infinity']

        # Increment time step
        time += 1

        # To prevent infinite loops, stop if cows are not moving
        if not east_cows and not north_cows:
            break

    # Output the result for each cow
    for result in results:
        print(result)

# Input number of cows and their data
num_cows = int(input())
cow_data = [input().split() for _ in range(num_cows)]

# Call the function to simulate and print results
simulate_cows(num_cows, cow_data)


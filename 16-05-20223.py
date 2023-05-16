start_state = [
    ['X', 'X', 'X', 'X', '.'],
    ['X', '.', '.', '.', '.'],
    ['X', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['X', 'X', '.', 'X', 'X']
]

# Assign tile numbers to each tile
grid_size = 5
tile_number = 0
tile_numbers = [[0] * grid_size for _ in range(grid_size)]
for row in range(grid_size):
    for col in range(grid_size):
        tile_numbers[row][col] = tile_number
        tile_number += 1

# Print the grid with tile numbers
for row in range(grid_size):
    for col in range(grid_size):
        print(start_state[row][col], end=' ')
    print("  ", end='')
    for col in range(grid_size):
        print(tile_numbers[row][col], end=' ')
    print()

layouts = {}

minute = 0
while True:
    # Convert the grid back to a string representation
    layout = ''.join(''.join(row) for row in start_state)

    # Check if the layout has been encountered before
    if layout in layouts:
        first_appearance_minute = layouts[layout]
        break

    # Store the current minute for the layout
    layouts[layout] = minute

    # Create a copy of the start_state for updating
    new_state = [row.copy() for row in start_state]

    # Iterate over each tile in the grid
    for i in range(25):
        row, col = divmod(i, 5)
        adjacent_count = 0

        # Check the four adjacent tiles
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = row + dr, col + dc

            # Skip if the adjacent tile is outside the grid
            if not (0 <= new_row < 5 and 0 <= new_col < 5):
                continue

            # Count the adjacent lifeforms
            if start_state[new_row][new_col] == 'X':
                adjacent_count += 1

        # Update the tile based on the rules
        if start_state[row][col] == 'X' and adjacent_count != 1:
            new_state[row][col] = '.'
        elif start_state[row][col] == '.' and adjacent_count in (1, 2):
            new_state[row][col] = 'X'

    # Update the start_state for the next minute
    start_state = new_state.copy()
    minute += 1

lifeform_score = sum(2 ** tile_num for tile_num, tile_value in enumerate(layout) if tile_value == 'X')
print("Lifeform score:", lifeform_score)

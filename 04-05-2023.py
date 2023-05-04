def find_floor(instructions):
    '''
    This function takes in a string of instructions and returns the floor that John
    ended up on. Each character in the string represents a move, where "<" means
    to go up one floor and ">" means to go down one floor. John starts on the ground
    floor (floor 0).
    
    Parameters:
        instructions (str): a string of instructions for John's movements
        
    Returns:
        int: the floor that John ended up on'''
    
    floor = 0
    for char in instructions:
        if char == "<":
            floor += 1
        elif char == ">":
            floor -= 1
    return floor

instructions = '''<<<<<<><><><><<<<><><><><><<<<><><><><><>>>><<><><><><><><><><>>>><<<<
<><><><><><<<<<><><><><><><<<<><><><><><><><><><><><<<<<<><><<><><>>><
<>><<><<>><><<><><><><><><><<<<<<<<<>><<><><<<><><><><<<<<<>>>>>>>>>>>
<>><><><>><<<><><><><<><><<><><><><><><><<<<><><><>><<>>>>><><><>><<<>
<><><><><><>><><><><><><><><><><><><><><><><><<<><><><><><><><><><><><
><><><><><><>>>><><><><><><><><><>><<<<<<<<<<>>>>><<<<<>>>><<<<>><<><<
><><><><><><><><><><<<<<<<><><<><<><<><<><><><><><<>><><>><><><><><<><
<<<<>><<<<><><<<><>>><<><>>>>><>>><<><<><><><><<>><><><><><><><><><><>
<><><><><><<<<><><<<<><<<>>>>>>>>><<><<<>>>>><<<<<<<<<>>>><<><>><><<><
<>><<>><<>><'''

current_floor = find_floor(instructions)
print(f"John is on floor {current_floor}")
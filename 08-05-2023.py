from itertools import permutations

def permutation_average(string):
    """
    Finds the average of the smallest and largest permutation of an integer string that is divisible by 7.

    Args:
    string (str): The integer string to find permutations of.

    Returns:
    float: The average of the smallest and largest permutation of the integer string that is divisible by 7,
           or None if there is no such permutation.
    """

    # Get all permutations of the integer string
    perms = permutations(string)
    
    # Check each permutation if it is divisible by 7
    valid_perms = []
    for perm in perms:
        num = int(''.join(perm))
        if num % 7 == 0:
            valid_perms.append(num)

    # If there are no valid permutations, return None
    if not valid_perms:
        return None

    # Calculate the average of the smallest and largest valid permutations
    smallest = min(valid_perms)
    largest = max(valid_perms)
    average = (smallest + largest) / 2

    return average
result = permutation_average('1867')
print(f"The average of the smallest and largest permutation divisible by 7 is {result}")
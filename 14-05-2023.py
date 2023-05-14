import re

def repeated_char(nodes: str) -> str:
    """
    Simplify repeated characters in a string of nodes.

    Parameters:
    nodes (str): A string of nodes.

    Returns:
    str: A string of nodes with repeated characters simplified.
    """
    for char in "abcdefghijklmnopqrstuvwxyz":
        nodes = re.sub(f"{char}+", char, nodes)
    return nodes

def find_lowest_count(nodes: str) -> tuple:
    """
    Find the node with the lowest count in a string of nodes.

    Parameters:
    nodes (str): A string of nodes.

    Returns:
    tuple: A tuple containing the lowest count of any node and the node to be removed.
    """
    nodes = repeated_char(nodes)
    lowest_count = float('inf')
    removed_node = ""
    for char in "abcdefghijklmnopqrstuvwxyz":
        count = nodes.count(char)
        if count > 0 and count < lowest_count:
            lowest_count = count
            removed_node = char
    return lowest_count, removed_node

def disconnect_nodes(nodes: str) -> int:
    """
    Remove nodes from a string in a way that minimizes the number of steps.

    Parameters:
    nodes (str): A string of nodes.

    Returns:
    int: The minimum number of steps required to disconnect the nodes.
    """
    total_steps = 0
    while nodes:
        steps, removed = find_lowest_count(nodes)
        total_steps += steps
        nodes = nodes.replace(removed, "")
        print(f"Step {total_steps}: Remove {removed} -> Remaining: {nodes}")
    return total_steps
nodes = '''kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor'''

steps = disconnect_nodes(nodes)
print(f"\nTotal Steps: {steps}")
efficiency = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111, 123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]


def costs(efficiency):
    # Sort the list of efficiencies
    sorted_efficiencies = sorted(efficiency)
    
    # Create an empty list to store the costs for each configuration
    costs = []
    
    # Iterate over each efficiency in the sorted list
    for i, current_efficiency in enumerate(sorted_efficiencies):
        
        # Create a new list of efficiencies that excludes the current efficiency
        other_efficiencies = sorted_efficiencies[:i] + sorted_efficiencies[i+1:]
        
        # Create a list of pairs of adjacent efficiencies
        pairs = [(other_efficiencies[j], other_efficiencies[j+1]) for j in range(0, len(other_efficiencies)-1, 2)]
        
        # Calculate the cost of each pair and sum them up
        cost = sum([abs(pair[0] - pair[1]) for pair in pairs])
        
        # Add the cost to the list of costs
        costs.append(cost)
    
    # Return the minimum cost
    return costs
min_cost = min(costs(efficiency))
print(f"the minimum cost is {min_cost}")
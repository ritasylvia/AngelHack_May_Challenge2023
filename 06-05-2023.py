runners = [
    ("John", 10, 6, 20),
    ("James", 8, 8, 25),
    ("Jenna", 12, 5, 16),
    ("Josh", 7, 7, 23),
    ("Jacob", 9, 4, 32),
    ("Jerry", 5, 9, 18)
]

total_time = 1234


def distance_covered(speed, run_duration, rest_duration, total_time):
    
    """
    Calculates the distance covered by a runner who alternates between running at a certain speed for a certain duration
    and resting for a certain duration, over a given total time.

    Args:
    - speed (int): the runner's speed in meters per second.
    - run_duration (int): the duration of the runner's running phase in seconds.
    - rest_duration (int): the duration of the runner's resting phase in seconds.
    - total_time (int): the total duration of the race in seconds.

    Returns:
    - int: the total distance covered by the runner in meters.
    """
    distance = 0
    running = True
    time_elapsed = 0
    
    while time_elapsed < total_time:
        if running:
            distance += speed * min(run_duration, total_time - time_elapsed)
            time_elapsed += run_duration
            running = False
        else:
            time_elapsed += rest_duration
            running = True
            
    return distance


distances = {}
for runner in runners:
    name, speed, run_duration, rest_duration = runner
    distances[name] = distance_covered(speed, run_duration, rest_duration, total_time)

winner = max(distances, key=distances.get)
print(f"The winning runner is {winner} with a total distance of {distances[winner]} meters.")
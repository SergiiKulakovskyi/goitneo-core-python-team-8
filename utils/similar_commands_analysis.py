from Levenshtein import distance

def find_most_similar_command(command, commands):
    """Returns the most similar command from a list of commands. The max Levenshtein distance is 2"""
    if command in commands:
        return command
    else:
        closest_commands = [x for x in commands if distance(command, x) <= 2]
        if closest_commands:
            return min(closest_commands, key=lambda x: distance(command, x))
        else:
            return None

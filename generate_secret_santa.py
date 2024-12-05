import random

def generate_matching(participants):
    """Generates a Secret Santa matching guaranteed to form a perfect cycle."""
    names = [person["name"] for person in participants]
    phones = {person["name"]: person["phone"] for person in participants}

    while True:
        random.shuffle(names)  # Shuffle the names
        matches = {names[i]: names[(i + 1) % len(names)] for i in range(len(names))}

        # Verify if it forms a perfect cycle
        visited = set()
        current = names[0]
        for _ in range(len(names)):
            if current in visited:
                break
            visited.add(current)
            current = matches[current]

        if len(visited) == len(names) and current == names[0]:
            # It's a perfect cycle
            break

    # Prepare output data
    output_data = {
        "matches": [
            {"gifter": gifter, "recipient": matches[gifter], "phone": phones[gifter]}
            for gifter in matches
        ]
    }
    return output_data

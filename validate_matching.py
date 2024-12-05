def validate_matching(participants, matching_data):
    """Validates that a matching is correct: no repeats, everyone included, and a perfect cycle."""
    try:
        participant_names = [person["name"] for person in participants]
        matches = {match["gifter"]: match["recipient"] for match in matching_data["matches"]}

        # Check if everyone is included as gifter and recipient
        gifters = set(matches.keys())
        recipients = set(matches.values())

        if set(participant_names) != gifters:
            return False
        if set(participant_names) != recipients:
            return False

        # Check for a perfect cycle
        visited = set()
        current = participant_names[0]
        for _ in range(len(participant_names)):
            if current in visited:
                return False
            visited.add(current)
            current = matches[current]

        # Final check to ensure cycle closes
        return current == participant_names[0]

    except Exception:
        return False

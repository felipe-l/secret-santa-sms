import json

def validate_matching(matching, participants):
    """
    Validates that all participants are in the matching, 
    that no one is giving to themselves, and that each person appears only once.
    """
    participant_names = {participant["name"] for participant in participants}
    gifter_names = set()
    recipient_names = set()

    for match in matching["matches"]:
        gifter = match["gifter"]
        recipient = match["recipient"]

        # Check if gifter and recipient are in the list of participants
        if gifter not in participant_names or recipient not in participant_names:
            return False

        # Check if gifter is not giving to themselves
        if gifter == recipient:
            return False

        # Check if each person appears only once as a gifter and recipient
        if gifter in gifter_names or recipient in recipient_names:
            return False

        gifter_names.add(gifter)
        recipient_names.add(recipient)

    # Ensure all participants are included in the matching
    if gifter_names != participant_names or recipient_names != participant_names:
        return False

    return True

# Read participants from JSON file
with open('participants.json', 'r') as f:
    participants_data = json.load(f)
    participants = participants_data["participants"]

# Read matching from JSON file
with open('matchings.json', 'r') as f:
    matching_data = json.load(f)

# Validate the matching
is_valid = validate_matching(matching_data, participants)
print("Is the matching valid?", is_valid)



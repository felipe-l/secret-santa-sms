import json
from generate_secret_santa import generate_matching
from validate_matching import validate_matching
from send_sms import send_sms

def load_participants(file_path):
    """Loads participants from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)["participants"]

def run_tests(participants, num_tests=100):
    """Runs test cases to validate the matching logic."""
    print(f"Running {num_tests} test cases...")
    for i in range(num_tests):
        test_matching = generate_matching(participants)
        if not validate_matching(participants, test_matching):
            print(f"Test case #{i + 1} failed.")
            return False
    print("All test cases passed successfully!")
    return True

def main():
    participants_file = "participants.json"
    final_matchings_file = "matchings.json"

    # Load participants
    participants = load_participants(participants_file)

    # Run tests (this step can be disabled by commenting the next line)
    if not run_tests(participants):
        print("Tests failed. Aborting process.")
        return

    # Generate the final matching
    print("Generating final Secret Santa matching...")
    final_matching = generate_matching(participants)
    with open(final_matchings_file, "w") as file:
        json.dump(final_matching, file, indent=4)
    print(f"Final matching saved to {final_matchings_file}")

    # Validate the final matching
    if not validate_matching(participants, final_matching):
        print("Validation of the final matching failed. Aborting!")
        return
    print("Final matching validated successfully!")

    # Send SMS notifications
    print("Sending SMS notifications...")
    send_sms(final_matching)

if __name__ == "__main__":
    main()

# Secret Santa Automation

This project automates the process of organizing a Secret Santa event. It includes generating matchings, validating them, and sending SMS notifications to participants.

## Project Structure

- **`main.py`**: The main script to run the Secret Santa process.
- **`generate_secret_santa.py`**: Contains logic to generate a Secret Santa matching.
- **`validate_matching.py`**: Validates the generated matching to ensure correctness.
- **`send_sms.py`**: Sends SMS notifications to participants using the Telnyx API.
- **`requirements.txt`**: Lists the Python dependencies required for the project.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**

   Create a `.env` file in the root directory with the following variables:

   ```plaintext
   TELNYX_API_KEY=your_telnyx_api_key
   FROM_NUMBER=your_telnyx_phone_number
   ```

5. **Prepare Participants Data:**

   Create a `participants.json` file with the following structure:

   ```json
   {
     "participants": [
       {"name": "Alice", "phone": "+1234567890"},
       {"name": "Bob", "phone": "+0987654321"},
       ...
     ]
   }
   ```

## Usage

1. **Run the Main Script:**

   Execute the main script to generate matchings, validate them, and send SMS notifications:

   ```bash
   python main.py
   ```

2. **Testing:**

   The script includes a testing phase to ensure the matching logic is correct. This can be disabled by commenting out the relevant line in `main.py`.

## Notes

- Ensure your Telnyx account is set up and you have a valid API key and phone number.
- The SMS sending functionality relies on the Telnyx API, so ensure your account has sufficient credits.
- The `requests` library is included in the `requirements.txt` for potential future use or extensions.

## License

This project is licensed under the MIT License.
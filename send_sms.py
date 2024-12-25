import telnyx
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your Telnyx API key from environment variable
telnyx.api_key = os.getenv("TELNYX_API_KEY")

# Define the sender number from environment variable
FROM_NUMBER = os.getenv("FROM_NUMBER")


def send_sms(matchings_data):
    """Sends SMS notifications to all Secret Santa participants using Telnyx."""
    for match in matchings_data["matches"]:
        to_number = match["phone"]
        gifter = match["gifter"]
        recipient = match["recipient"]
        message_text = f"Hola {gifter}, eres el Santa Secreto de {recipient} para el Fambam 2024. ¡Le darás un regalo a {recipient}! Mantenlo en secreto 🎁."

        # Attempt to send the message
        try:
            message = telnyx.Message.create(
                from_=FROM_NUMBER,
                to=to_number,
                text=message_text
            )
            print(f"Message to {gifter} sent successfully!")
            print(f"Message ID: {message.id}")
        except Exception as e:
            print(f"Failed to send message to {gifter} ({to_number}):", str(e))

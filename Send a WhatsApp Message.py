import pywhatkit as kit
import datetime

def send_whatsapp_message(phone_number, message, hour, minute):
    """
    Sends a WhatsApp message to the specified phone number at the given time.
    
    :param phone_number: str : Recipient's phone number in the format '+<country_code><phone_number>'
    :param message: str : The message to send
    :param hour: int : The hour (24-hour format) to send the message
    :param minute: int : The minute to send the message
    """
    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        print(f"Message sent to {phone_number}: {message} at {hour}:{minute}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input details
    phone_number = input("Enter the recipient's phone number (including country code): ")
    message = input("Enter your message: ")
    
    # Get the current time
    now = datetime.datetime.now()
    
    # Schedule the message to send 1 minute from now
    hour = now.hour
    minute = now.minute + 1  # Schedule to send 1 minute from now

    # Send the WhatsApp message
    send_whatsapp_message(phone_number, message, hour, minute)

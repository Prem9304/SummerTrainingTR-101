import pywhatkit as kit

# Get user input for recipient's phone number, message, and time
recipient_phone_number = input("Enter recipient's phone number (with country code, e.g., +1234567890): ")
message = input("Enter the message you want to send: ")

# Get user input for the hour and minute to schedule the message
hour = int(input("Enter the hour (0-23) to send the message: "))
minute = int(input("Enter the minute (0-59) to send the message: "))

# Send the message using pywhatkit
kit.sendwhatmsg(recipient_phone_number, message, hour, minute)
print(f"Message scheduled to be sent to {recipient_phone_number} at {hour:02d}:{minute:02d}")

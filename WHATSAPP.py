import pywhatkit as kit

recipient_phone_number = input("Enter recipient's phone number (with country code, e.g., +1234567890): ")
message = input("Enter the message you want to send: ")

hour = int(input("Enter the hour (0-23) to send the message: "))
minute = int(input("Enter the minute (0-59) to send the message: "))

kit.sendwhatmsg(recipient_phone_number, message, hour, minute)
print(f"Message scheduled to be sent to {recipient_phone_number} at {hour:02d}:{minute:02d}")

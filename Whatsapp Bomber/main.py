import pywhatkit as kit
import time

def send_multiple_whatsapp_messages(phone_number, message, num_times, interval):
    """
    Sends a WhatsApp message multiple times to a specified phone number.
    
    :param phone_number: str, recipient phone number with country code, e.g., "+1234567890"
    :param message: str, message to send
    :param num_times: int, number of times to send the message
    :param interval: int, time interval in seconds between messages
    """
    
    i=num_times-1;
    for _ in range(num_times):
        try:
        # Get the current time and schedule the message for the next minute\
            print("Bombing started...........")
            current_time = time.localtime()
            hour = current_time.tm_hour
            minute = current_time.tm_min + 1
            
            # Send the message
            kit.sendwhatmsg_instantly(phone_number, message)
            
            print(f"Message sent to {phone_number}: {message}")
            
            print(f"Message Remaining : {i}")
            i=i-1
            
            # Wait for the specified interval before sending the next message
            time.sleep(interval)
            
        except Exception as e:
            print(f"Failed to send Message {i}: {str(e)}")
        
        
        #
        # print(f"Message sent to {phone_number}: {message}")

if __name__ == "__main__":
    #phone_number = "+1234567890"  # Replace with the recipient's phone number
    phone_number = "+916280117780"
    
    #message = "This is an automated message sent using Python."  # Replace with your message
    message = "Padbichiye"
    
    num_times = 10
    # Specify the number of times you want to send the message
    #interval = 60  # Time interval in seconds between messages (e.g., 60 seconds)
    interval = 2
     
    send_multiple_whatsapp_messages(phone_number, message, num_times, interval)
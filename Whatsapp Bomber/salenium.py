from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def send_whatsapp_message(phone_number, message, count, delay_between_msgs):
    # Initialize WebDriver
    chrome_driver_path = "C:/Users/ajay1/OneDrive/Desktop/drivers/chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_path)  # Ensure chromedriver is in your PATH or specify its path here
    driver.get("https://web.whatsapp.com")
    
    # Wait for user to scan the QR code
    input("Press Enter after scanning QR code and WhatsApp Web is loaded completely...")

    # Open the chat with the specified phone number
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
    search_box.send_keys(phone_number)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)  # Wait for the chat to load
    
    for i in range(count):
        try:
            #message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='1']")
            message_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-tab='6'] div[contenteditable='true']")))

            message_box.send_keys(message)
            message_box.send_keys(Keys.ENTER)
            print(f"Message {i+1} sent successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(delay_between_msgs)
    
    driver.quit()

if __name__ == "__main__":
    phone_number = "+916284046869"  # Replace with the recipient's phone number
    message = "Hello from Selenium!"  # Replace with your message
    count = 5  # Number of times to send the message
    delay_between_msgs = 5  # Delay in seconds between each message
    
    send_whatsapp_message(phone_number, message, count, delay_between_msgs)

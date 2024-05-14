from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os
from tensorflow.keras.models import load_model
import pyautogui
import time
import serial

#creating a list of all the foods, in the argument i put the path to the folder that has all folders for food
def create_foodlist(path):
    list_ = list()
    for root, dirs, files in os.walk(path, topdown=False):
      for name in dirs:
        list_.append(name)
    return list_    

#loading the model i trained and finetuned        
my_model = load_model('model_trained.h5', compile = False)
food_list = create_foodlist("food-101/images") 


# Open the serial port
ser = serial.Serial('COM9', 9600)

# Define a function to close the serial port
def close_serial_port():
    if ser.is_open:
        ser.close()

# Define a function to predict the class from a screenshot and control the motor
def predict_class_screen(model, show=True):
    # Define the region to capture
    screen_width, screen_height = pyautogui.size()
    region = (screen_width // 4, screen_height // 4, screen_width // 2, screen_height // 2)  # Center region

    
    screenshot = pyautogui.screenshot(region=region)
    screenshot = screenshot.resize((299, 299))

    img = np.array(screenshot, dtype=np.float64)  # Convert to float64 here
    img = np.expand_dims(img, axis=0)
    img /= 255.                                      

    pred = model.predict(img)
    index = np.argmax(pred)
    food_list.sort()
    pred_value = food_list[index]
    
    if 'chocolate' in pred_value.lower():
        print("yesbefore")
        ser.write(b'1')  
        print("yes")

    if show:
        plt.imshow(img[0])
        plt.axis('off')
        plt.title(pred_value)
        plt.show()

# Example usage
try:
    for i in range(5):
        print("PREDICTIONS BASED ON SCREEN CONTENT")
        predict_class_screen(my_model, True)
        time.sleep(10)
finally:
    close_serial_port()  # Close the serial port when finished





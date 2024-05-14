import serial
import time
from tensorflow.keras.preprocessing import image
# from tenserflow.contrib.keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os
from tensorflow.keras.models import load_model

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

# Initialize serial connection
ser = serial.Serial('COM9', 9600)  # Update 'COM9' with your Arduino's port


def predict_class(model, images, show=True):
    for img_path in images:
        img = image.load_img(img_path, target_size=(299, 299))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img /= 255.

        pred = model.predict(img)
        index = np.argmax(pred)
        pred_value = food_list[index]

        # Send signal to Arduino if chocolate is predicted
        if 'chocolate' in pred_value.lower():
            print("yesbefore")
            ser.write(b'1')  
            print("yes");
            

        if show:
            plt.imshow(img[0])
            plt.axis('off')
            plt.title(pred_value)
            plt.show()
            
        time.sleep(5)

        

        # Close serial connection
    ser.close()


#add the images you want to predict into a list (these are in the WD)
images = [ 'sam.jpg','1033790.jpg', 'mouse.jpg']

# Predict and send signals to Arduino
print("PREDICTIONS BASED ON PICTURES UPLOADED")
predict_class(my_model, images, True)

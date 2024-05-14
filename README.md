
* **The dataset being used is [Food 101] (download it here https://www.kaggle.com/dansbecker/food-101)** 
* **Use tensorflow-gpu for faster training time** 

* **You need to have the food-101 dataset in your working directory (otherwise you should change the paths to the food-101 file)** 
- Run data_preparation.py to create the train set and test set from the dataset.
- Run Model.py to tune and train the model ( a MobileNetV2 Pretrained model is used and tuned to the food-101 dataset ) 
- Run Prediction_food_images.py to predict new food images. ( the images to be predicted here were in the working directory, if you have them in another location you should change the path)
- Run Prediction_food_fromScreen.py to predict food images present on the screen(It runs for 5 times and captures images every 10 sec which can be changed as per requirement)

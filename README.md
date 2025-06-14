# Viral Social Media Trend Predictor

## Overview
This project predicts the engagement level (High, Medium, Low) of social media posts based on features like platform, region, hashtag category, trending status, posting hour, and day of the week.

## Dataset
- Source: Public dataset titled "Viral_Social_Media_Trends.csv"
- Features include: Platform, Region, Hashtag, Trending, Post Hour, Day of the Week, Engagement Level
- Cleaned and encoded categorical variables for model training.

## How to Run

### Setup
Dependencies for the project are listed in the requirements.txt file and include:
- pandas
- numpy
- scikit-learn
- joblib
. tk (for the GUI interface)

A virtual environment is recommended for managing dependencies, but not required.
Model Training
The training process is handled by the train_model.py script. This script reads the dataset,
performs preprocessing (defined in preprocess.py ), trains a K Neighbors Classifier , and saves the
resulting model as engagement_mode1.pk1 using joblib.

Graphical User Interface
After training, the gui_app.py script provides a simple interface for users to input post
characteristics and receive a predicted engagement level. The GUI uses the trained model file and
expects all input fields to match the format used during training.

## Project Structure
project/
--
- Viral_Social_Media_Trends.csv # Raw dataset
- train_model.py # Model training script
- preprocess.py # Preprocessing logic
- gui_app.py # GUI application for prediction
- engagement_model.pkl # Trained model file
- requirements.txt # Python library dependencies
- README.md # Project documentation

## License 
- This project is provided for educational purposes.


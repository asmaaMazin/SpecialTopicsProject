
import streamlit as st   #build a web app interface
import pandas as pd      #to handle taular data
import joblib            #to load the previously trained and save model

#load the trained model
model = joblib.load("engagement_model.pkl")

#Encoding dictionaries
platform_map  = {'TikTok':1,'Instagram':2,'YouTube':3,'Twitter':4}

region_map = {'UK':1,'Japan':2,'USA':3,'Canada':4,'Brazil':5,'Australia':6,'Germany':7,'India':8}

hashtag_map = {'Challenge': 1, 'Comedy': 2, 'Dance': 3, 'Education': 4, 'Fation': 5,}

#App UI
st.title("Viral Social Media Trend Predictor")
st.write("Enter post details to predict the engagement level")

#input widgets
platform = st.selectbox("Platform", list(platform_map.keys()))

region = st.selectbox("Region", list(region_map.keys()))

hashtag = st.selectbox("Hashtag Category", list(hashtag_map.keys()))

#Convert selected strings to corresponding numeric values 
platform_num = platform_map[platform]

region_num = region_map[region]

hashtag_num = hashtag_map[hashtag]

#Create input DataFram for Prediction
input_data = pd.DataFrame([{'Platform':platform_num, 'Hashtag': hashtag_num, 'Region':region_num}])

#Show input
st.write("preview of Encoded input")
st.dataframe(input_data)

#prediction block
#when the predict button clicked the model predicts a class and that numbber is mapped back to its string label
if st.button("Predict Engagement Level"):
    try:
        engagement_map_reverse = {0: 'High', 1: 'Medium', 2: 'Low'}
        prediction = model.predict(input_data)[0] 
        predicted_label = engagement_map_reverse.get(prediction, "Unknown")

        st.success(f"Predicted Engagement Level:{predicted_label} (Class:{prediction})")
    except Exception as e:
        st.error(f"Prediction error:{e}")
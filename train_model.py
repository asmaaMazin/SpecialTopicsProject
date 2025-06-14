import pandas as pd                                                   #for data loading and manipulation
# import matplotlib.pyplot as plt                                       
from sklearn.model_selection import train_test_split, GridSearchCV    #devide data into training and test sets
from sklearn.neighbors import KNeighborsClassifier                    #a basic classification algorithm that predicts based on nearest data input
from sklearn.preprocessing import LabelEncoder                        #converts categorical text labels into numeric values
import joblib                                                         #for saving and loading the trined model

#load dataset 
df = pd.read_csv("Viral_Social_Media_Trends.csv")

#Encode categorical features
le_hashtag = LabelEncoder()
le_platform = LabelEncoder()
le_region = LabelEncoder()
le_engagement = LabelEncoder()

#converts string column into numbeic values 
df['Hashtag'] = le_hashtag.fit_transform(df['Hashtag'])
df['Platform'] = le_platform.fit_transform(df['Platform'])
df["Region"] = le_region.fit_transform(df['Region'])
df['Engagement_Level'] = le_engagement.fit_transform(df['Engagement_Level'])

#prints the mapping used for engagement levels this helps in revers the prediction in GUI
print(dict(zip(le_engagement.classes_,le_engagement.transform(le_engagement.classes_))))

#Define features and target 
X =df[['Platform', 'Hashtag', 'Region']]   #input features the nodel will learan from
y = df['Engagement_Level']                 #what the model will try to predict

#split data 80% for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

#hyperparameter tuning with GridSearchCV
param_grid = {'n_neighbors': [3, 5, 7, 9]}                         #finds the best n_neighbors value that gives the highest accuracy on average
grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv = 5)
grid.fit(X_train, y_train)

print("Best parameters form GridSearchCV:", grid.best_params_)

#use the best model
best_model = grid.best_estimator_

#save the best model
joblib.dump(best_model, "engagement_model.pkl")
print("Optimized model saved as engagement_model.pkl")









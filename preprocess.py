
import pandas as pd

#load the raw dataset
df = pd.read_csv("Viral_Social_Media_Trends.csv")

#Drop rows with missing values
df.dropna(inplace = True)

#mapping dictionaries
plasfrom_map  = {'TikTok':1,'Instagram':2,'YouTube':3,'Twitter':4}

region_map = {'UK':1,'Japan':2,'USA':3,'Canada':4,'Brazil':5,'Australia':6,'Germany':7,'India':8}

hashtag_map = {'Challenge': 1, 'Comedy': 2, 'Dance': 3, 'Education': 4, 'Fation': 5,}

engagemnet_map = {'Hight': 1, 'Medium': 2, 'Low': 3}

#Apply mappings
df['Platform'] = df['Platform'].map(plasfrom_map)
df['Region'] = df['Region'].map(region_map)
df['Hashtag'] = df['Hashtag'].map(hashtag_map)
df['Engagement_Level'] = df['Engagement_Level'].map(engagemnet_map)

#save cleaned dataset
df.to_csv("Viral_Social_Media_Trends_cleaned.csv",index=False)

print("Data cleaned and save to Viral_Social_Media_Trends_cleaned.csv") 



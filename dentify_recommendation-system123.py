#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]


##Step 1: Read CSV File
df = pd.read_csv("Dataset_AreTeethHealthy?.csv")


#print df.columns
##Step 2: Select Features

features = ['Tooth-pain','color-teeth','cavities','sensitivity-during-sweet-or-cold','bad-breath','bleeding-gums','tongue-color','teeth-not-alligned']
##Step 3: Create a column in DF which combines all selected features
for feature in features:
	df[feature] = df[feature].fillna('')

def combine_features(row):
	try:
		return row['Tooth-pain'] +" "+row['color-teeth']+" "+row['cavities']+" "+row['sensitivity-during-sweet-or-cold']+""+row['bad-breath']+""+row['bleeding-gums']+""+ row['tongue-color'] +" "+row['teeth-not-alligned']
	except:
		print ("Error:", row	)

df["combined_features"] = df.apply(combine_features,axis=1)

#print "Combined Features:", df["combined_features"].head()

##Step 4: Create count matrix from this new combined column
cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])

##Step 5: Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix) 
tooth_disorders = "x"

## Step 6: Get the index of this tooth disorder
user_index = get_index_from_tooth_disorders(tooth_disorders)

similar_tooth =  list(enumerate(cosine_sim[user_index]))

## Step 7: Get a list of similar movies in descending order of similarity score
sorted_similar_tooth_disorders = sorted(similar_tooth,key=lambda x:x[1],reverse=True)

## Step 8: Print titles of first 50 movies
i=0
for element in sorted_similar_tooth_disorders:
		print(get_tooth_disorder_from_index(element[0])) 
		i=i+1
		if i>50:
			break

            


# In[30]:


cd Dentify_Recommendation-System.ipynb


# In[10]:


pwd


# In[3]:


import pandas as pd


# In[4]:


import pandas as pd


# In[18]:


pd.read_csv("Dataset_AreTeethHealthy?.csv")


# In[ ]:





import pandas as pd 
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import os 
class sentiment_analyzer:
	def check_sentiment(self,raw_text):
            self.raw_text = raw_text
            os.chdir('/home/jeelan/dataset')
            df1 = pd.read_csv('Womens Clothing E-Commerce Reviews.csv')
            df = df1[['Review Text','Rating','Class Name','Age']]
            df['Review Text'] = df['Review Text'].fillna('')

# CountVectorizer() converts a collection 
# of text documents to a matrix of token counts
            vectorizer = CountVectorizer()
# assign a shorter name for the analyze
# which tokenizes the string
            analyzer = vectorizer.build_analyzer()
            df = df[df['Rating'] != 3]
            df['Sentiment'] = df['Rating'] >=4
            train_data,test_data = train_test_split(df,train_size=0.8,random_state=0)
            X_train = vectorizer.fit_transform(train_data['Review Text'])
            y_train = train_data['Sentiment']
            nb = MultinomialNB()
            nb.fit(X_train,y_train)
            print(nb.predict(vectorizer.transform([raw_text])))

sentiment1 = sentiment_analyzer()

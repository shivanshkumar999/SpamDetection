# -*- coding: utf-8 -*-
"""SPAM SMS Detection

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TGfyc10UQPghtDcP2AO-hrhgFfv1-UCI
"""

import pandas as pd, numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
import string

nltk.download('punkt')
nltk.download('stopwords')

data = pd.read_csv('/content/spam.csv', encoding='ISO-8859-1')
data.head()

# @title v1

from matplotlib import pyplot as plt
import seaborn as sns
data.groupby('v1').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

x = data['v2']
y = data['v1']





def preprocess(data):
  final_data=[]
  for i in range(len(data)):

    data[i] = data[i].lower()

    tokens = word_tokenize(data[i])

    tokens = [ token for token in tokens if token not in string.punctuation]

    stop_words = set(stopwords.words('english'))

    tokens = [token for token in tokens if token not in stop_words]

    final_data.append(" ".join(tokens))

  return final_data

x = preprocess(x)

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
x = cv.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.35, random_state=42)

x_train[0:5]

model = LogisticRegression()
model.fit(x_train, y_train)
y_pred=model.predict(x_test)

y_pred

y_pred=pd.Series(y_pred)

y_pred.value_counts()

input = "Congratulations! You've won a free vacation to Hawaii. Claim your prize now"

input = cv.transform([input]).toarray()
out = model.predict(input)

print(out)
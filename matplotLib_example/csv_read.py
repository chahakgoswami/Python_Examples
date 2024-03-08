from collections import Counter as ctr
from matplotlib import pyplot as plt 
import pandas as pd


language_counter = ctr()
data = pd.read_csv('..\\files\\data.csv')
lang_response = data['LanguagesWorkedWith']
for row in lang_response:
    language_counter.update(row.split(';'))

languages = []
count=[]
for item in language_counter.most_common(15):
    languages.append(item[0])
    count.append(item[1])

languages.reverse()
count.reverse()
plt.barh(languages,count)
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.legend()
plt.title('Languages VS Popularity')
plt.tight_layout()
plt.show()   
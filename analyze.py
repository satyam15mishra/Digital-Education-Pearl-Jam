import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

## loading the dataset

data = pd.read_csv('learnvern.csv')


# Checking for null values
data.isnull()

# Grabing the informations from the dataset
data.head()

data.describe()

data.tail()



print(data.columns)  



melt = pd.melt(data,id_vars='learnvernfeedback',value_vars=['raisedhands','VisitedResources','viewingannouncements'])



sns.swarmplot(x='variable',y='value',hue='learnvernfeedback' , data=melt,palette={'H':'lime','M':'grey','L':'red'})
plt.ylabel('Values from zero to 100')
plt.title('High, middle and low level students')

#plt.show()    Figure_1


data['numeric_class'] = [1 if data.loc[i,'learnvernfeedback'] == 'L' else 2 if data.loc[i,'learnvernfeedback'] == 'M' else 3 for i in range(len(data))]


# Now lets look at nationality
nation = data.NationalITy.unique()
nation_grades_ave = [sum(data[data.NationalITy == i].numeric_class)/float(len(data[data.NationalITy == i])) for i in nation]
ax = sns.barplot(x=nation, y=nation_grades_ave)
jordan_ave = sum(data[data.NationalITy == 'Jordan'].numeric_class)/float(len(data[data.NationalITy == 'Jordan']))
print('Jordan average: '+str(jordan_ave))
plt.xticks(rotation=90)

#plt.show()     figure_2
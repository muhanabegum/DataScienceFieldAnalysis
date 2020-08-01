#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
import matplotlib.pyplot as plt     
import numpy as np                      
from scipy.sparse import csr_matrix     
get_ipython().run_line_magic('matplotlib', 'inline')


# In[81]:


csv_file = 'Downloads/Kaggle Sample Data/DataAnalystJobs.csv'
names = ['Job Title', 'Salary Estimate', 'Rating', 'Company Name', 'Location', 'Headquarters', 'Size', 'Industry', 'Sector', 'Revenue' ]


# In[82]:


rawdata = read_csv(csv_file, names=names)


# In[83]:


# Basic overview of the first 10 columns in the data file
rawdata.head(10)


# In[84]:


# Getting the average rating at a data science/analyst position
rawdata["Rating"].mean()


# In[90]:


chart = rawdata['Sector'].value_counts().plot(kind='bar', title="Common Sectors for Data Analyst Jobs")
chart.set_xlabel("Sector")
chart.set_ylabel("Count")
plt.show()


# In[86]:


# Minimum rating for a position. Note that a rating of -1 is assumed to be where no information was available
rawdata['Rating'].min()


# In[87]:


# Max rating of a position (out of 5)
rawdata['Rating'].max()


# In[70]:


# Information on the top rated data analyst job
rawdata.loc[rawdata['Rating'].idxmax()]


# In[88]:


# Information on one of the lowest rated jobs
rawdata.loc[rawdata['Rating'].idxmin()]

# After interpreting this, we can see that it is just missing inputs 


# In[89]:


# Counts of the different values in the 'Sector' column 
print(rawdata.groupby('Sector').size())

# Note that sector '-1' simply means no information was reported 


# In[93]:


# Printing top 10 industries 
print(rawdata.groupby('Industry').size().nlargest(10))


# In[95]:


# Printing top 10 job locations 
print(rawdata.groupby('Location').size().nlargest(10))


# In[100]:


# Bar chart on the top 25 job locations 
chart2 = rawdata['Location'].value_counts().nlargest(25).plot(kind='bar', title="Top 25 Locations for Data Analyst Jobs")
chart2.set_xlabel("Location")
chart2.set_ylabel("Count")
plt.show()


# In[112]:


# Print out the top 5 occuring salary bracket to understand a sort of common/average pay 
common_pay = rawdata.groupby('Salary Estimate').size().nlargest(5)
print(common_pay)


# In[119]:


print(rawdata.groupby('Size').size())


# In[121]:


# Breakdown of company size 
chart3 = rawdata['Size'].value_counts().plot(kind='bar', title="Top 25 Locations for Data Analyst Jobs")
chart3.set_xlabel("Location")
chart3.set_ylabel("Count")
plt.show()


# In[141]:


# Breakdown of Company Size 
frequency = rawdata.groupby(["Size"]).size()
plt.pie(frequency, labels=sums.index, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Breakdown of Company Size")
plt.axis('equal')
plt.show()


# In[143]:


rawdata


# In[145]:


New_York = rawdata[rawdata.Location == 'New York, NY']


# In[151]:


# Pie chart of company sizes 
frequency2 = New_York.groupby(["Size"]).size()
plt.pie(frequency2, labels=sums.index, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Breakdown of Company Size in New York for Data Analyst Jobs")
plt.axis('equal')
plt.show()


# In[153]:


# List of the top 10 companies that employ data analysts according to this survey 
print(rawdata.groupby('Company Name').size().nlargest(10))


# In[155]:


# Top 10 companies that employ data analaysts in New York according to this survey 
print(New_York.groupby('Company Name').size().nlargest(10))


# In[163]:


# Comparing New York's rating with the entire data
print(New_York["Rating"].mean())
print(rawdata["Rating"].mean())


# In[169]:


# Job titles that were used for this data file 
titles = rawdata.groupby('Job Title').size().nlargest(10)
print(titles)


# In[175]:


# Table of company revenue yearly 
print(rawdata.groupby('Revenue').size())


# In[176]:


# Breakdown of company revenue 
chart4 = rawdata['Revenue'].value_counts().plot(kind='bar', title="Yearly Revenue of Companies")
chart4.set_xlabel("Revenue")
chart4.set_ylabel("Count")
plt.show()


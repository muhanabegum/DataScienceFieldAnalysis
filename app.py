import streamlit as st
import altair as alt
import pandas as pd
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
import matplotlib.pyplot as plt     
import numpy as np                      
from scipy.sparse import csr_matrix

st.sidebar.markdown("# A Little Bit About Me")
st.sidebar.markdown("## Hi, I'm Muhana Begum!")
st.sidebar.markdown("I am a 2nd year electrical engineering student at the University of Waterloo and I enjoy working with data and creating visualizations, whether it's for websites, data, or simply presentations.")
st.sidebar.markdown("As a data enthusiast, I hope you enjoy this webpage/dashboard that I created where I use **Python** and **Streamlit** to present visualizations and my own personal analysis on the data science/analyst job market before the global pandemic of 2020.") 
st.sidebar.markdown("If you have any questions, please feel free to email me at **m6begum@uwaterloo.ca**")
st.sidebar.markdown("For more fun stuff created by me, check out my github at **www.github.com/muhanabegum** and my LinkedIn at **www.linkedin.com/in/muhana-begum**")

st.title("Data Visualizations of the Data Science Job Market")
st.header("**Webpage created by Muhana Begum**")

st.info("This dataset was found on **Kaggle** titled ***Data Analyst Jobs*** and uploaded by **Larxel**. Please check out his Kaggle page for more.")
st.write("***Note that I have edited the csv file to be simpler and contain only relevent/important information. I hope you enjoy my analysis!***")

csv_file = "https://raw.githubusercontent.com/muhanabegum/DataScienceFieldAnalysis/master/DataAnalystJobs.csv"
names = ['Job Title', 'Salary Estimate', 'Rating', 'Company Name', 'Location', 'Headquarters', 'Size', 'Industry', 'Sector', 'Revenue' ]
rawdata = pd.read_csv(csv_file, names=names)

st.subheader("Introduction")
st.write("Due to the corona virus, developer & data science jobs have shown a decline as employees were laid off and hiring freezes occured. Data science/analyst positions were scraped from Glassdoor here and I will analyze the information to understand more about this field prior to the global pandemic.")
st.write("Below is the full table of information. You can also expand it to get a fullscreen view.")

st.subheader("Full Data Table")
st.write(rawdata)

st.subheader("Job Ratings")
st.write("First, let's calculate the maximum and miniumm ratings positions were given by employees.")
if st.checkbox("Click to see the max and min ratings of these positions."):
	st.write("Max: ", rawdata['Rating'].max(), " ", "Min: ", rawdata['Rating'].min())
	st.warning("Note: It is important to realize here that a rating of -1 could either mean severe dissatisfaction or there wasn't any information inputted by an employee. In addition, the scale for ratings goes from 0 to 5.0")

st.write("Let's take a deeper look into one of the top rated jobs:")
st.write(rawdata.loc[rawdata['Rating'].idxmax()])

st.subheader("Sector")
st.write("To gain a better understanding on each of these categories, let's focus on one of the most important ones; the sector the job fits into.")
st.write("Below is a chart showing all the sectors the jobs from the dataset are in.")
sector_info = rawdata['Sector'].value_counts()
st.bar_chart(sector_info)

if st.checkbox("Click to see the information above in table format."):
	st.write(sector_info)

st.success("**Information Technology** and **Business Services** are easily the most popular sectors for data analysis and data science. Skills like Python, R, SQL and others are important in making business decisions from company data and are also prominent among people who work in technology/software. ")
st.warning("Also note here that **-1** is assumed to exist because information was not available for certain jobs.")

st.markdown("## Let's analyze more of the data and get some basic conclusions.")

st.subheader("Top 10 Job Titles")
titles = rawdata['Job Title'].value_counts().nlargest(10)
st.write(titles)

st.subheader("Top 10 Industry")
top_industries = rawdata['Industry'].value_counts().nlargest(10)
st.bar_chart(top_industries)

st.subheader("Top 10 Location")
top_locations = rawdata['Location'].value_counts().nlargest(10)
st.bar_chart(top_locations)

st.subheader("Top 5 Estimated Salary")
common_pay = rawdata['Salary Estimate'].value_counts().nlargest(5)
st.write(common_pay)

st.subheader("Top 10 Companies With Their Average Rating")
All_Companies = rawdata['Company Name'].value_counts().nlargest(10)
st.write(All_Companies)

st.subheader("Company Size (by number of employees)")
company_size = rawdata['Size'].value_counts()
st.bar_chart(company_size)

st.subheader("Annual Company Revenue")
revenue = rawdata['Revenue'].value_counts()
st.write(revenue)
st.warning("Note: It is safe to assume that revenue of -1 is the same as Unknown / Not Applicable.")

st.markdown("## Based on the charts and metrics above, let's focus on **New York** as it seems to be one of the most popular locations for data science jobs. ")
st.write("We can isolate for just New York data in Python by: ")
st.code("New_York = rawdata[rawdata.Location == 'New York, NY']")
New_York = rawdata[rawdata.Location == 'New York, NY']
frequency2 = New_York["Size"].value_counts()
st.subheader("Size of Companies in New York")
st.bar_chart(frequency2)

st.subheader("Now let's focus on the job ratings between New York and the entire data.")
st.write("New York: ", New_York["Rating"].mean(), "Full Data: ", rawdata["Rating"].mean())
st.info("When comparing to all locations, New York tends to be right around the average.")

st.markdown("## This concludes the data web page and I hope you learned a few things about the data science/analyst field.")
st.markdown("## For more of my personal projects and information about me, please check out the panel on your right.")

links = st.selectbox("Click below for some of my contacts/links!", ["Email", "Github", "LinkedIn", "Website"])

if links == 'Email':
	st.success("m6begum@uwaterloo.ca")
if links == 'Github':
	st.success("www.github.com/muhanabegum")
if links == 'LinkedIn':
	st.success('www.linkedin.com/in/muhana-begum')
if links == 'Website': 
	st.success("www.muhanabegum.me")

st.title("")
st.title("")

if st.button("CLICK ME FOR A MESSAGE!"):
	st.title("Thank you for visiting!")

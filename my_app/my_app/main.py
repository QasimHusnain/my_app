import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Pakistan Zindabad")
st.text("Live long Pakistan, Live long Pakistan")
#streamlit = "^1.37.1"
df = pd.DataFrame({'col1':[1,2,3], 'col2':list('abs'),'col3':["Qasim","Husnain","SE"]})
st.write(df) # 👈 Draw the dataframe
x : int = 100
'x', x  # 👈 Draw the string 'x' and then the value of x
# Also works with most supported chart types
arr = np.random.normal(1, 1, size=100) # 1: The mean of the distribution.
#1: The standard deviation of the distribution.
# size=100: The number of random values to generate
fig, ax = plt.subplots()
ax.hist(arr, bins=30)
fig 
# d_csv = pd.read_csv('customers-100.csv')
# st.write(d_csv)
# x = d_csv['Model']
# y = d_csv['price'] 
# plt.xlabel('Model')
# plt.ylabel('price')

plt.show()

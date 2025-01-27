
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# Loading datasets
customers  = pd.read_csv('Dataset\\Customers.csv')
products  = pd.read_csv('Dataset\\Products.csv')
transactions  = pd.read_csv('Dataset\\Transactions.csv')


# Merginig dataset
transactions_customers_info = pd.merge(transactions, customers, on="CustomerID", how="inner")
final_dataset = pd.merge(transactions_customers_info, products, on="ProductID", how="inner")


final_ops = final_dataset.copy()

# Cleaning the data if possible
print(final_ops.isnull().sum())
print(final_ops.duplicated())

# Feature Engineering
transact = final_ops.groupby('').agg({
     
})


# Calculating Similarity


# Recommendations


print(final_ops.columns.array)




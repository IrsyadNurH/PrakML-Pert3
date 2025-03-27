#Modul 3: Data Cleaning dan Transformation

# %%
import pandas as pd

# %%
# Membaca dataset
data = pd.read_csv("students.csv")

# %%
# Menampilkan 10 baris pertama
print(data.head(10))

# %%
# Show the dataset info
data.info()

# %%
# Missing Value Checking
data.isna().sum()

# %%
# Filling Nan Value with mode
data['lunch'].fillna(data['lunch'].mode()[0], inplace=True)


#%%
# Filling Nan Value with mean
data['reading score'].fillna(data['reading score'].mean(), inplace=True)

# %%
# Filling Nan Value with mode
data['grade'].fillna(data['grade'].median(), inplace=True)

# %%
# Check the information of the dataset
data.info()

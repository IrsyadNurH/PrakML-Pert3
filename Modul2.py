import pandas as pd

# Membaca dataset
data = pd.read_csv("DatasetForCoffeeSales2.csv")

# Menampilkan 10 baris pertama
print("\nMenampilkan 10 baris pertama:")
print(data.head(10))

# Filter data untuk menampilkan kolom yang dipilih
filtered_data = data.filter(["City", "Category", "Product", "Quantity"])
print("\nData yang sudah difilter:")
print(filtered_data.head())

# Mengurutkan berdasarkan Quantity (dari terbesar)
data.sort_values("Quantity", axis=0, ascending=False, inplace=True, na_position="last")
print("\nData setelah diurutkan berdasarkan Quantity:")
print(data.head())

# Mengelompokkan Total Sales berdasarkan City
grp1 = data.groupby('City')
result = grp1['Final Sales'].aggregate('sum')
print("\nTotal Penjualan per Kota:")
print(result)
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

!!wget 'https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx'
df = pd.read_excel('Online Retail.xlsx')
df.dropna(subset=['Description', 'CustomerID'], inplace=True)

transactions = df.groupby('InvoiceNo')['Description'].apply(list)

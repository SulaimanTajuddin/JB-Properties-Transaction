import chardet # for automatically detect the character encoding of files
import pandas as pd # for data manipulation and analysis

# Detect the encoding
with open('JB Properties Data 2021-2024 (TSV).csv', 'rb') as f: # rb: read binary mode
    result = chardet.detect(f.read()) # analyzes the raw bytes to guess the character encoding
    print(f"Detected encoding: {result['encoding']}") # print the encoding result

# Load TSV with detected encoding
df = pd.read_csv('JB Properties Data 2021-2024 (TSV).csv', sep='\t', encoding=result['encoding'])

print(df.head(5))                      # print output of the first n row
print(df.dtypes)                       # print output of the data types by column
print("\n(Total no. of rows, Total no. of columns) = " + f"{df.shape}")
print("\nNull values (True/False):\n") 
print(df.isnull())                     # Check for null values in all cell, returns print output True/False for each cell
print("\nTotal sum of duplicated values = " + f"{df.duplicated().sum()}")





#!./bin/python3
from email.mime import nonmultipart
from importlib import import_module
import pandas as pd

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
imported_file = "/home/ubuntu/codes/data-science/ibm-course/data/imports-85.data"
# df = pd.read_csv(url, header = None)
df = pd.read_csv(imported_file, header = None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers

print(df.head(10))

export_path = "/home/ubuntu/codes/data-science/ibm-course/exports/automobile.csv"

df.to_csv(export_path)
print('*****')
print(df.dtypes)
print('*****')
print(df.describe(include = 'all'))
print('*****')
print(df.info())



import geopandas
import geoplot
import sqlite3
import csv
import pandas as pd


con = sqlite3.connect('FPA_FOD_20170508.sqlite')
cur = con.cursor()

data = pd.read_sql_query('SELECT FIRE_NAME, FIRE_SIZE_CLASS, LATITUDE, LONGITUDE FROM Fires WHERE STATE=\'OR\' OR STATE=\'CA\' OR STATE=\'WA\'', con)

print(data.head())
print(data.tail())
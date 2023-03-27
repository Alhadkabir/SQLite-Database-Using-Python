import pandas as pd
from pandas import DataFrame
import psycopg2 as psy

conn = psy.connect(
    database="python sql",
    host="localhost",
    user="alhad",
    password="alhad",
    port="5432")

sql = "SELECT * FROM PLAYERS"

df = pd.read_sql(sql,conn)

print(df)

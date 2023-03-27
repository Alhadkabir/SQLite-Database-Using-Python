import pandas as pd
from pandas import DataFrame
import psycopg2 as psy

conn = psy.connect(
    database="python sql",
    host="localhost",
    user="user",//this is the user name of your db
    password="user",//this is the password of your db
    port="5432")

sql = "SELECT * FROM PLAYERS"

df = pd.read_sql(sql,conn)

print(df)

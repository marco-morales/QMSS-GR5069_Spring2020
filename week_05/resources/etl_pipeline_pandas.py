# Databricks notebook source
# MAGIC %md # WORKSHOP - Data Pipeline in Practice

# COMMAND ----------

# MAGIC %md ##### Step 1 - Read in Dataset

# COMMAND ----------

import pandas as pd 
import datetime as dt
from io import BytesIO
import boto3

# COMMAND ----------

s3 = boto3.client(
    's3',
    aws_access_key_id='',
    aws_secret_access_key=''
)

# COMMAND ----------

bucket = "ne-gr5069"
f1_lap_times = "raw/lap_times.csv"

obj_laps = s3.get_object(Bucket= bucket, Key= f1_lap_times) 
df_laptimes = pd.read_csv(obj_laps['Body'])
len(df_laptimes)

# COMMAND ----------

f1_drivers = "raw/drivers.csv"
obj_driver = s3.get_object(Bucket= bucket, Key= f1_drivers) 
df_drivers = pd.read_csv(obj_driver['Body'])
len(df_drivers)

# COMMAND ----------

# MAGIC %md #### Transform Data 

# COMMAND ----------

df_drivers['dob'] = pd.to_datetime(df_drivers['dob']).dt.date

# COMMAND ----------

display(df_drivers)

# COMMAND ----------

df_drivers['age'] = (dt.datetime.now().date() - df_drivers['dob'])/366
df_drivers['age'] = df_drivers['age'].dt.days.astype('int16')

# COMMAND ----------

df_driver_laptimes = pd.merge(df_drivers, df_laptimes, on='driverId', how='inner')

# COMMAND ----------

len(df_driver_laptimes)

# COMMAND ----------

# MAGIC %md #### Aggregate Data by Age

# COMMAND ----------

df_laptime_age = df_driver_laptimes[df_driver_laptimes['age'] < 30]

# COMMAND ----------

df_laptime_age_agg = df_laptime_age.groupby('age').agg({'milliseconds':['mean']})

# COMMAND ----------

df_laptime_age_agg

# COMMAND ----------

# MAGIC %md #### Storing Data to S3

# COMMAND ----------

session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
)

# COMMAND ----------

s3 = session.resource('s3')
csv_buffer = StringIO()
df_laptime_age_agg.to_csv(csv_buffer)
s3 = session.resource('s3')
s3.Object(bucket, 'interim/by_age_laptimes_pandas.csv').put(Body=csv_buffer.getvalue())

# COMMAND ----------



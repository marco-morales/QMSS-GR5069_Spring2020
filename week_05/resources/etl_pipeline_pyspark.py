# Databricks notebook source
# MAGIC %md # WORKSHOP - Data Pipeline in Practice

# COMMAND ----------

# MAGIC %md ##### Step 1 - Read in Dataset

# COMMAND ----------

from pyspark.sql.types import DateType,IntegerType
from pyspark.sql import functions as F

# COMMAND ----------

df_laptimes = spark.read.csv('/mnt/ne-gr5069/raw/lap_times.csv',header=True)
df_laptimes.count()

# COMMAND ----------

display(df_laptimes)

# COMMAND ----------

df_drivers = spark.read.csv('/mnt/ne-gr5069/raw/drivers.csv',header=True)
df_drivers.count()

# COMMAND ----------

display(df_drivers)

# COMMAND ----------

# MAGIC %md #### Transform Data 

# COMMAND ----------

df_drivers = df_drivers.withColumn("dob", df_drivers["dob"].cast(DateType()))
df_drivers = df_drivers.withColumn("age", F.datediff(F.current_date(),F.col("dob"))/366)


# COMMAND ----------

display(df_drivers)

# COMMAND ----------

df_drivers = df_drivers.withColumn("age", df_drivers["age"].cast(IntegerType()))

# COMMAND ----------

display(df_drivers)

# COMMAND ----------

df_driver_laptimes = df_drivers.select('driverId','driverRef','forename','surname','dob','age').join(df_laptimes, on=['driverId'])

# COMMAND ----------

# MAGIC %md #### Aggregate Data by Age

# COMMAND ----------

df_laptime_age = df_driver_laptimes.filter(F.col('age') < 30)

# COMMAND ----------

display(df_laptime_age.groupby('age').agg(F.avg('milliseconds')).orderBy('age'))

# COMMAND ----------

# MAGIC %md #### Storing Data to S3

# COMMAND ----------

df_laptime_age.write.csv('/mnt/ne-gr5069/interim/by_age_laptimes.csv')

# COMMAND ----------



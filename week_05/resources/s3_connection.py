# Databricks notebook source
ACCESS_KEY = ""
# Encode the Secret Key as that can contain "/"
SECRET_KEY = "".replace("/", "%2F")
AWS_BUCKET_NAME = ""
MOUNT_NAME = ""

dbutils.fs.mount("s3a://%s:%s@%s" % (ACCESS_KEY, SECRET_KEY, AWS_BUCKET_NAME), "/mnt/%s" % MOUNT_NAME)
display(dbutils.fs.ls("/mnt/%s" % MOUNT_NAME))

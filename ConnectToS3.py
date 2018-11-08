#!/usr/bin/env python
# coding=utf-8
 
 
import boto3
import os
 
 
access_key = "xx"
secret_key = "xx"
endpoint_url = "https://s3-ganesha101.r-local.net"
 

# Establish the session.
s3 = boto3.client(
    service_name = "s3",
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_key,
    endpoint_url = endpoint_url
)
connection_type = "client"
 
 
# Create bucket.
s3.create_bucket(Bucket = "Frontend")
 
 
# Show list of buckets.
buckets = s3.list_buckets()
d = {k:v for k, v in buckets.items() if k in "Buckets"}
for i in d["Buckets"]:
    for x,y in i.items():
        if x in "Name":
            print(y)
 
 
# Store "~/banana.png" file to the bucket.
put_key = "banana.png"
stored_file_name = put_key
s3.upload_file(stored_file_name, "Frontend", put_key)
 
 
# Show all files in the bucket.
objects = s3.list_objects_v2(Bucket = "Frontend")
for i in objects["Contents"]:
    for x,y in i.items():
        if x in "Key":
            print(y)
 
 
# Download "banana.png" file from the bucket and store under "/tmp/".
get_key = "banana.png"
download_file_name = "/tmp/" + get_key
s3.download_file("Frontend", get_key, download_file_name)
 
 


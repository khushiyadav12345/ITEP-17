# 1. Read and Modify First Word

# Using r+ mode:

# Create a file containing:

# Hello World
# Replace Hello with Hi


import requests
import json
import os

print(os.getcwd())
response = requests.get("https://dummyjson.com/products")

json_response = response.json()

print(json_response)

def write_api_response(data):
    try:
        with open("file-handling/file-collection/product.json","w") as f:
            json.dump(data,f,indent=4)
            print("Operation Success")
    except Exception as e:
       print(e)
       
write_api_response(json_response)

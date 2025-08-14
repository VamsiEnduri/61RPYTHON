# contractor :-- 20 
# contractor :-- 5
# team :-- 


# python :-- owner :-- money ( concpets , syntax)
# third party libraries  :-- requests

# modules :-- 
# piece of prefefined methods r functions 

# inbuilt modules (random, math, datetime, re)
# user defined
# third party modules (requests)
# text, json, get, post, put,delete, status_code, headers etc..

# pip install requests

import requests

# print(requests,"abc")

apiURL="https://fakestoreapi.com/products"

response=requests.get(apiURL)

print(type(response.json()))
print(type(response.text))

print(response.status_code,"code")
# print(requests.get(apiURL),"get request")

if response.status_code == 200 :
    jsonData=response.json()
    # print(jsonData,"data")
    for i in range(len(jsonData)):
        for j in jsonData[i].values():
            print(j)
        # if a[i]
        # print(jsonData[i]["title"],"pr")
        # print(jsonData[i]["image"],"img")
        # if jsonData[i]["category"] == "electronics":
        #     print(jsonData[i]["title"],"elec title")

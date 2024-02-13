import os

import requests
from datetime import datetime
import os

token_pixela=os.environ.get("tokenpixela")
username=os.environ.get("nameofuser")
pixela_endpoint="https://pixe.la/v1/users"

parameters={
    "token":token_pixela,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
# post_req=requests.post(url="https://pixe.la/v1/users", json=parameters)
# print(post_req.text)
graph_ID="firstgraph"
graph_config={
    "id":"firstgraph",
    "name":"Calorie graph",
    "unit":"calories",
    "type":"int",
    "color":"ajisai"
}
headers={
    "X-USER-TOKEN":token_pixela
}
# graph_end=f"{pixela_endpoint}/{username}/graphs"
# response=requests.post(url=graph_end,json=graph_config,headers=headers)
# print(response.text)
today=datetime.now()
today_date=datetime.strftime(today.date(), '%Y%m%d')



post_pixel={
   "date":today_date,
   "quantity":input("How many calories did you ate today?")
}

graph_end=f"{pixela_endpoint}/{username}/graphs/{graph_ID}"
response=requests.post(url=graph_end, json=post_pixel,headers=headers)
print(response.text)

# put_pixel={
#     "quantity":"2850"
# }
# resource=requests.put(url=graph_end, json=put_pixel, headers=headers)
# print(resource.text)

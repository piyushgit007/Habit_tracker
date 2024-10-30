from http.client import responses

import requests


USERNAME = "dev23"
TOKEN = "gjdsnjfdnfadad21321dac"
GRAPH_ID = "graph2"

pixela_endpoint = "https://pixe.la/v1/users"

user_params ={
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling graph",
    "unit" : "Km",
    "type" : "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint,json = graph_config,headers = headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date" : "20241029",
    "quantity": "15"
}


# response = requests.post(url=pixel_creation_endpoint,json = pixel_data,headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20241029"
pixel_updated_data = {
    "quantity" : "4"
}

# response = requests.put(url=pixel_update_endpoint,json=pixel_updated_data,headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20241029"

# response = requests.delete(url=pixel_delete_endpoint,headers=headers)
# print(response.text)

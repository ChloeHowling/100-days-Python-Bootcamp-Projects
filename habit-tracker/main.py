import requests
from datetime import datetime, timedelta

USERNAME = "chloehltam"
TOKEN = "sdfghjk856t"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "mile",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
today = datetime.now()
yesterday = datetime.now() - timedelta(1)

block_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
block_params = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "5.1",
}

# response = requests.post(url=block_endpoint, json=block_params, headers=headers)
# print(response.text)
put_endpoint = f"{block_endpoint}/{yesterday.strftime('%Y%m%d')}"
put_params = {
    "quantity": "0.1"
}

# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)

delete_endpoint = f"{block_endpoint}/{yesterday.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
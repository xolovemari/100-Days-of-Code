import requests
from datetime import datetime

USERNAME = "example"
TOKEN = "example"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Studying Graph",
    "unit": "Hours",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"https://pixe.la/v1/users/example/graphs/graph1"

today = datetime(year=2025, month=2, day=7)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "7"
}

response = requests.put(url=pixel_update, json=new_pixel_data, headers=headers)
print(response.text)
from    dotenv      import load_dotenv
from    datetime    import datetime  
import  requests
import  os

load_dotenv()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
MY_TOKEN = os.getenv("MY_TOKEN")
USERNAME = os.getenv("USERNAME")
GRAPHID = "graph1"

user_params = {
    "token": MY_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": MY_TOKEN
}

# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_endpoint = f"{PIXELA_ENDPOINT}/thiago0333/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Programming Time",
#     "unit": "minutes",
#     "type": "float",
#     "color": "ajisai"
# }


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHID}"
# pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/thiago0333/graphs/{GRAPHID}"

# today = datetime.now()

# pixel_data = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "1.00",
# }

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


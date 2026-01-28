#APIs
import requests

# Making an HTTP request
response = requests.get("https://google.com")

# Server responds with data
if response.status_code == 200:
    print("Got the data!")
    data = response.json()
 

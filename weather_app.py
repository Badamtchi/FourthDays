import requests

# api-endpoint
URL = f"https://api.openweathermap.org/data/2.5/weather"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'q':'Tehran', 'appid':'316eee88398f7a6b46f14afe1fbb1321'}
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
  
# extracting data in json format
data = r.json()
print(data)
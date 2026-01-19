import requests
from urllib.parse import urlencode



class HttpRequestsrequestser:

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self, params) -> None:
        if not isinstance(params, dict):
            raise TypeError("Params have dict")
        self.params = params
        
    def fetch(self):
        query_string = urlencode(self.params)
        url = f"{self.BASE_URL}?{query_string}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise Exception(str(error))

import requests

class FlightSearch:
    def __init__(self):
        self.api_url = "example"
        self.token = self._get_access_token()
        self.header = {"Authorization": f"Bearer {self.token}"}

    def _get_access_token(self):
        auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        auth_data = {
            "grant_type": "example",
            "client_id": "example",
            "client_secret": "example",
        }
        response = requests.post(auth_url, data=auth_data)
        response.raise_for_status()
        return response.json()["access_token"]

    def flight_search(self, destination, departure_date, return_date):
        params = {
            "originLocationCode": "GIG",
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
        }
        response = requests.get(self.api_url, params=params, headers=self.header)
        response.raise_for_status()
        return response.json()
import requests

class DataManager:
    def __init__(self):
        self.url = "example"
        self.valid_codes = ["GIG", "GRU", "BSB"]  # Códigos suportados na sandbox

    def get_row(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json().get("price", [])

    def add_city(self, city, code, budget):
        if code not in self.valid_codes:
            raise ValueError(f"Código IATA inválido: {code}")
            
        params = {
            "price": {
                "city": city,
                "iataCode": code,
                "lowestPrice": budget,
            }
        }
        response = requests.post(self.url, json=params)
        response.raise_for_status()
        return response.json()

    def modify_price(self, row_id, new_lowest_price):
        update_url = f"{self.url}/{row_id}"
        params = {"price": {"lowestPrice": new_lowest_price}}
        response = requests.put(update_url, json=params)
        response.raise_for_status()
        return response.json()
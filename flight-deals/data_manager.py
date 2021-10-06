from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/3c75b974a9671147f405a3644dcf0a08/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/3c75b974a9671147f405a3644dcf0a08/flightDeals/users"
HEADER = {
    "Authorization": "Bearer sedfdgfhjkiou839yurhjkhk"
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADER)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=HEADER
            )
            print(response.text)

    def get_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=HEADER)
        data = response.json()
        emails = []
        for row in data['users']:
            emails.append(row['email'])
        return emails
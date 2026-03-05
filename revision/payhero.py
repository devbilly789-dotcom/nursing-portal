
import requests

class PayHeroSTK:
    def __init__(self, config):
        self.config = config
        self.base_url = "https://backend.payhero.co.ke/api/v2"

    def _make_request(self, endpoint, method="POST", params=None, payload=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.config["AUTH_TOKEN"]
        }
        try:
            if method == "POST":
                response = requests.post(url, headers=headers, json=payload)
            elif method == "GET":
                response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

    def initiate_stk_push(self, phone_number, amount, reference, customer_name="Customer"):
        if phone_number.startswith("0"):
            phone_number = "254" + phone_number[1:]
        payload = {
            "amount": amount,
            "phone_number": phone_number,
            "channel_id": self.config["CHANNEL_ID"],
            "provider": self.config["PROVIDER"],
            "external_reference": reference,
            "customer_name": customer_name,
            "callback_url": self.config["CALLBACK_URL"],
            "account_id": self.config["ACCOUNT_ID"]
        }
        return self._make_request("payments", payload=payload)

    def check_payment_status(self, reference):
        params = {"reference": reference}
        return self._make_request("transaction-status", method="GET", params=params)

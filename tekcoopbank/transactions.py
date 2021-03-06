"""
Transaction Status subclass of Bank.
"""
import requests
from . import bank


class TransactionStatus(bank.Bank):
    def send(self, messageReference, callback=None):
        token = self.token
        url = self.host + "/Enquiry/TransactionStatus/2.0.0"
        payload = {
            "MessageReference": messageReference,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.post(url, headers=headers,
                                 json=payload, verify=False)
        if callback is not None:
            return callback(response)
        else:
            return response

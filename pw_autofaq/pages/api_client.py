import requests

class APIClient:
    BASE_URL = 'https://chat.autofaq.ai/api/webhooks/widget/6c24eb52-b1ab-4d78-8463-8556d4ee04b3'

    def open_chat(self):
        response = requests.options(f'{self.BASE_URL}/start')
        return response


    def pass_user_details(self, payload):
        response = requests.post(f'{self.BASE_URL}/users', json=payload)
        return response
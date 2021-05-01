import json
import sys
from urllib.parse import urlencode

import requests as requests

sys.path.append('/Users/alan/')
from secret import *
import logging

logging.basicConfig(level=logging.DEBUG, filename="app.log")


def main():
    endpoint = NUTRITIONIX_EXERCISE_URL
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
        "Content-Type": "application/json",
    }
    post = {
        "query": "ran 5 kms, walked 2 km",
        "gender": "male",
        "weight_kg": 80.5,
        "height_cm": 173,
        "age": 40
    }

    params = urlencode(post)
    url = f"{endpoint}?{params}" #, data=json.dumps(post), headers=headers
    logging.debug(url)

    response = requests.post(endpoint, data=json.dumps(post), headers=headers)
    json_cs_data = json.loads(response.content)
    print(json.dumps(json_cs_data, indent=2))

if __name__ == '__main__':
    main()


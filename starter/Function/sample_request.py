"""
Start the Function locally before running this script
"""
import requests
import json

FUNCTION_URL = "https://springer.azurewebsites.net/api/SpringerLookup?" \
                "code=rd1wHutqW6AcArAE5bcOKuu1LcPuwatQJhacVL3ERtRJyN1hXse66A=="
LOCAL_URL = "http://localhost:7071/api/SpringerLookup"

req_body = {
    "Values": [
        {
            "RecordId": 0,
            "Data": {
                "ArticleName": "Machine learning for digital try-on: Challenges and progress"
                }
        }
    ]
}

response = requests.post(LOCAL_URL, json.dumps(req_body))
print(response.status_code)
print(response.content)

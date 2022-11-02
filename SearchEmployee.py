import requests
import json

headers = {
"Content-Type": "application/json",
"Connection": "keep-alive",
}

try :
    response = requests.get("https://uhwxroslh0.execute-api.us-east-1.amazonaws.com/dev/employee?id=1", headers=headers)
    print(response.status_code)
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(err)
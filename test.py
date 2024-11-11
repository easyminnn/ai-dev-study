import requests

url = "http://127.0.0.1:8000/predict"
text = "Movie is fun!"

response = requests.post(url, json={"text": text})
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
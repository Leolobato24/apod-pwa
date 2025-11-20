import requests

API_KEY = "TU_API_KEY"
ciudad = "León"
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print("Temperatura:", data["main"]["temp"], "°C")
print("Descripción:", data["weather"][0]["description"])

# alexis leonardo cazares lobato 
# lird402
# API REST 

import requests

ACCESS_KEY = "PuEK8c2qA2h-rebHQoWv7h7e5i0kdcAdm_7GMmjoHEs"
palabra = "cats"

# URL correcta con f-string
url = f"https://api.unsplash.com/search/photos?query={palabra}&client_id={ACCESS_KEY}"

# Hacer la solicitud GET
response = requests.get(url)

# Convertir la respuesta a formato JSON
data = response.json()

# Recorrer los resultados y mostrar los enlaces de las imágenes
for img in data["results"]:
    print(img["urls"]["small"])

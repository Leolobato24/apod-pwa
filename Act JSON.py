#Ricardo Josue Vazquez Lopez
#LIRD 402

import requests
 
ACCESS_KEY ="PuEK8c2qA2h-rebHQoWv7h7e5i0kdcAdm_7GMmjoHEs"
palabra = "cocktails"
 
 
url = f"https://api.unsplash.com/search/photos?query={palabra}&client_id={ACCESS_KEY}"
 
response = requests.get(url)
data = response.json()
 
for img in data["results"]:
     print(img["urls"]["small"])
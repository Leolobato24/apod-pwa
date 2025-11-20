#Alexis Leonardo Cazares Lobato 
# LIRD402 
#Actividad 1er equipo


import requests
 
# Tu clave personal para acceder a la API de Google
# ¡¡ADVERTENCIA: NO COMPARTAS ESTA CLAVE!!
API_KEY = "AIzaSyCBu9k7ernPr1lU7lwfSwQihwvAuIgAjzM"
 
# La dirección que quieres convertir a coordenadas
direccion = "León, Guanajuato, México" # Puedes cambiar esta dirección
 
# La URL del servicio de la API de Geocodificación, combinando la dirección y tu clave
url = f"https://maps.googleapis.com/maps/api/geocode/json?address={direccion}&key={API_KEY}"
 
print(f"Realizando solicitud a: {url}")
 
try:
    # Se realiza la petición HTTP al servidor de Google
    response = requests.get(url)
    response.raise_for_status() # Lanza una excepción para códigos de estado HTTP de error (4xx o 5xx)
 
    # Se convierte la respuesta (en formato JSON) a un diccionario de Python
    data = response.json()
 
    # Se revisa si la petición fue exitosa según el estado de la API
    if data['status'] == "OK":
        # Se extraen las coordenadas del diccionario de datos
        # El primer resultado suele ser el más relevante
        if data["results"]:
            ubicacion = data["results"][0]["geometry"]["location"]
            
            # Se imprimen la latitud y longitud
            print("\nUbicación encontrada:")
            print("Latitud:", ubicacion["lat"])
            print("Longitud:", ubicacion["lng"])
        else:
            print(f"No se encontraron resultados para la dirección: {direccion}")
    elif data['status'] == "ZERO_RESULTS":
        print(f"La API de Geocodificación no encontró resultados para la dirección: {direccion}")
    else:
        print(f"Error en la respuesta de la API. Estado: {data['status']}")
        if 'error_message' in data:
            print(f"Mensaje de error: {data['error_message']}")
 
except requests.exceptions.RequestException as e:
    print(f"Error al realizar la solicitud HTTP: {e}")
except ValueError as e:
    print(f"Error al decodificar la respuesta JSON: {e}")
except KeyError as e:
    print(f"Error al acceder a una clave en la respuesta JSON: {e}. La estructura de la respuesta puede haber cambiado o ser inesperada.") 
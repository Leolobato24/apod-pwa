# Alexis Leonardo Cazares Lobato 
# LIRD402 
# 13/11/2025

#PRACTICA DE EQUIPO DE JSON
import requests
import json

#Este programa escoge el nombre de un pokemon:
nombre = input("Escribe el nombre de un pokemon: ").lower()
url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

response = requests.get(url)
if response.status_code == 200:
    datos = response.json()
    print("Datos encontrados:")
    print(json.dumps(datos, indent=4, ensure_ascii=False))  # JSON legible

    print(f"\nNombre: {datos['name'].capitalize()}")
    print(f"Peso: {datos['weight']}")
    print(f"Altura: {datos['height']}")
else:
    print("No se encontró el pokemon.")
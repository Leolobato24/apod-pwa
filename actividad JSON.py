# Alexis Leonardo Cazares Lobato
# LIRD402
# 13/11/2025

{
    "name": 'Frieda',
    "address": {
        "work": null, // Doesn't pay rent either
        "home": 'Berlin',
    },
    "friends": [
        {
            "name": "Philipp",
            "hobbies": ["eating", "sleeping", "reading",],
        }
    ]
}
¿QUÉ TIENE MAL ESTE CÓDIGO?

Uso de comillas simples (' ')
JSON solo acepta comillas dobles " " en cadenas de texto.

Comentarios dentro del JSON (// ...)
JSON no permite comentarios de ningún tipo.

Comas finales extra (trailing commas)
Ejemplos:

"home": 'Berlin',

"reading",]
JSON no permite comas al final de la última propiedad o elemento.

Hay comas faltantes
Entre objetos, falta una coma después de cerrar "address".

El valor de texto 'Berlin' está entre comillas simples
Debe ser "Berlin".

El JSON completo no puede validarse por todos estos errores combinados.


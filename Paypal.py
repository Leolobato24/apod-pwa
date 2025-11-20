import requests

# Token de acceso (debes obtenerlo vía OAuth)
access_token = "TU_ACCESS_TOKEN"
url = "https://api.sandbox.paypal.com/v1/payments/payment"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

payload = {
    "intent": "sale",
    "payer": {"payment_method": "paypal"},
    "transactions": [{
        "amount": {"total": "10.00", "currency": "USD"},
        "description": "Pago de prueba"
    }],
    "redirect_urls": {
        "return_url": "https://example.com/success",
        "cancel_url": "https://example.com/cancel"
    }
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())

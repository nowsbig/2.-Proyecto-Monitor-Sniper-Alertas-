import requests, json

def obtener_precio_kraken(par):
    url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
    try:
        r = requests.get(url)
        #print(f"Status code: {r.status_code}")
        return r.json()
    except Exception as e:
        return f"Error detectado: {e}"
import requests, json, time

posicion = None

def obtener_precio_kraken(par):
    url = "https://api.kraken.com/0/public/Ticker?pair=XBTUSD"
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"Error en API: {e}")
        return None
import requests, json, time

class MonitorSniper:
    def __init__(self, par):
        self.par = par

    def check_price(self):
        url = f"https://api.kraken.com/0/public/Ticker?pair={self.par}"
        try:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()

            nombre_par = list(data['result'].keys())[0]
            precio_str = data['result'][nombre_par]['a'][0]
            precio_float = float(precio_str)
    
            return precio_float
        except Exception as e:
            print(f"Error en {self.par}: {e}")
            return None

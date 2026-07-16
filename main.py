import json, time, requests
from api_cliente import MonitorSniper
from alertas import evaluar_precio

monitor_btc = MonitorSniper("XXBTZUSD")
monitor_eth = MonitorSniper("XETHZUSD")

precio_btc = monitor_btc.check_price()
precio_eth = monitor_eth.check_price()

while True:
    precio_btc = monitor_btc.check_price()
    precio_eth = monitor_eth.check_price()

    if precio_btc and precio_eth is not None:
        print(f"\nPrecio BTC: {precio_btc}")
        print(f"Precio ETH: {precio_eth}")
        time.sleep(60)  # Esperar 60 segundos antes de la siguiente verificación
    else:
        print("Error al obtener el precio de uno o ambos activos.")

    time.sleep(10)  # Esperar 10 segundos antes de la siguiente verificación
print(f"Precio BTC: {precio_btc}")
print(f"Precio ETH: {precio_eth}")
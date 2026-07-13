import json, time, requests
from api_cliente import obtener_precio_kraken
from alertas import evaluar_precio

print("\nIniciando Monitor Sniper...")

while True:
    precio = obtener_precio_kraken('XXBTZUSD')
    precio_filtrado = precio['result']['XXBTZUSD']['a'][0]

    try:
        if precio is not None:
            precio_actual = float(precio_filtrado)
            print(f"\nPrecio: {precio_actual:.2f}")
            time.sleep(60)
        else:
            print("No se pudo obtener el precio. Reintentando en 60 segundos...")
    except:
        print("Esperando 60 segundos por reconexión...")
        time.sleep(60)
import json, time
from api_cliente import obtener_precio_kraken

print("\nIniciando Monitor Sniper...")

#datos = obtener_precio_kraken('XXBTZUSD')
#precio_actual = datos['result']['XXBTZUSD']['a'][0]

while True:
    try:
        dato = obtener_precio_kraken("XXBTZUSD")
        precio_actual = dato['result']['XXBTZUSD']['a'][0]
        precio_float = float(precio_actual)
        print(f"\nPrecio actual de BTC: {precio_float}")
        
        if precio_float < 60000:
            print(f"¡ALERTA! El precio está en zona de compra.")
        else:
            print(f"El precio aun no llega al objetivo. Manteniendo posición paiva.")
        
        time.sleep(60)
    except KeyboardInterrupt:
        print("\nMonitor detenido por el usuario.")
        break
    except Exception as e:
        print(f"Error inesperado: {e}")
        time.sleep(10)
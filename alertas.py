def evaluar_precio(precio_actual):
    if float(precio_actual) < 60000:
        return f"Alerta: ¡Oportunidad de compra!"
    return "Esperando zona de compra..."
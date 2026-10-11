import random
import json
import paho.mqtt.client as mqtt
import time
from datetime import datetime

broker = "localhost" 
port = 1883 
topic = "iot/raspberrypi/temperatura"

client = mqtt.Client() 
client.connect(broker, port, 60)

try:
    while True: 
        temperature = random.uniform(20.0, 30.0)
        
        # Obtener timestamp actual (formato ISO 8601)
        timestamp = datetime.now().isoformat()
        
        # Empaquetar en JSON (recomendado)
        payload = json.dumps({
            "timestamp": timestamp,
            "temperatura": round(temperature, 2)
        })
        
        print(f"Publicando -> {payload}")
        client.publish(topic, payload)
        time.sleep(5)

# Cerramos la aplicación con Ctrl+C
except KeyboardInterrupt:
    client.disconnect()
    print("Cerrando programa. Conexión cerrada")
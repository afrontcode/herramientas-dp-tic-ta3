from datetime import datetime, timezone
import json
import random
import ssl
import time
import paho.mqtt.client as mqtt

# Configuración del Broker y Credenciales de Autenticación
BROKER = "localhost"
PORT = 1883  # Puerto seguro TLS
USERNAME = "sensor_python"
PASSWORD = "CAMBIAR_ESTA_CLAVE"  # Asegúrate de crear este usuario en EMQX (http://localhost:18083)

# Definición de múltiples sensores simulados (recomendación de la guía)
SENSORES = [
    {"id": "sensor_01", "ubicacion": "Sala"},
    {"id": "sensor_02", "ubicacion": "Cocina"},
    {"id": "sensor_03", "ubicacion": "Exterior"},
]

# Inicialización del cliente MQTT (Callback API Version 2)
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2, client_id="nodo_iot_python"
)

# Configurar Autenticación por Usuario y Contraseña
client.username_pw_set(USERNAME, PASSWORD)

# Configurar TLS/SSL utilizando el certificado de la CA generado localmente
#client.tls_set(
#    ca_certs="broker/certs/ca.crt",
#    cert_reqs=ssl.CERT_REQUIRED,
#    tls_version=ssl.PROTOCOL_TLS_CLIENT
#)

# Conexión al Broker MQTT seguro
#client.connect(BROKER, PORT, keepalive=60)
#client.loop_start()

try:
  while True:
    for sensor in SENSORES:
      # Generación de variables ambientales simuladas
      temperatura = round(random.uniform(20.0, 30.0), 2)
      humedad = round(random.uniform(40.0, 80.0), 2)
      presion = round(random.uniform(1005.0, 1025.0), 2)

      # Obtener timestamp actual en formato ISO 8601 (UTC)
      timestamp = datetime.now(timezone.utc).isoformat()

      # Estructura de datos en JSON
      payload = json.dumps({
          "sensor_id": sensor["id"],
          "ubicacion": sensor["ubicacion"],
          "temperatura": temperatura,
          "humedad": humedad,
          "presion": presion,
          "timestamp": timestamp,
      })

      topic = f"iot/{sensor['id']}/mediciones"
      print(f"Publicando en [{topic}] -> {payload}")

      # Publicación con QoS 1
      client.publish(topic, payload, qos=1)

    # Pausa de 5 segundos entre ciclos
    time.sleep(5)

except KeyboardInterrupt:
  client.loop_stop()
  client.disconnect()
  print("Cerrando programa. Conexión cerrada.")
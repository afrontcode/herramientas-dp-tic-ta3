## TA Semana 10 - Grupo 4 - Broker MQTT EMQX

### 1. Ejecución del Broker

```powershell
docker compose up -d
docker ps
```

### 2. Acceder al panel

http://localhost:18083

Usuario: admin
Contraseña: public

Nos será solicitado generar una nueva contraseña

### 3. Seguir los pasos de instalación y ejecución del simulador del sensor 

Ver carpeta sensor-dht22-simulado/

### 4. Verificar la transmisión de datos mediante MQTT Explorer, MQTTX u otro cliente MQTT

Host: localhost:1883
Tópico: iot/raspberrypi/temperatura

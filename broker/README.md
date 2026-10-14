## TA Semana 10 - Grupo 4 - Broker MQTT EMQX

### 1. Ejecución del Broker

El servicio/programa Docker debe estar funcionando antes de ejecutar los siguientes comandos:

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
Tópico: iot/# (cada sensor publica en iot/<sensor_id>/mediciones, p. ej. iot/sensor_01/mediciones)

### 5. Seguridad: autenticación por usuario y contraseña

Por defecto EMQX acepta conexiones anónimas. Para exigir credenciales:

1. En el panel ir a **Access Control → Authentication → Create**.
2. Mecanismo: **Password-Based**. Backend: **Built-in Database**. Dejar los valores por defecto (`username`, hash `sha256`) y pulsar **Create**.
3. En la fila del autenticador creado pulsar **Users → Add** y crear el usuario:
   - Username: `sensor_python`
   - Password: la misma que se coloque en `MQTT_PASSWORD` del archivo `.env` del sensor
4. Crear también un usuario para el cliente de verificación (MQTT Explorer / MQTTX), por ejemplo `explorer`.

A partir de ese momento cualquier cliente sin usuario válido es rechazado (`Not authorized`), en todos los puertos.

### 6. Seguridad: cifrado TLS/SSL (puerto 8883)

El listener `ssl:default` usa los certificados de `certs/`:

| Archivo      | Uso                                                  |
|--------------|------------------------------------------------------|
| `ca.crt`     | Autoridad certificadora del laboratorio (la usan los clientes para validar al broker) |
| `server.crt` | Certificado del broker (CN=localhost, SAN localhost / 127.0.0.1) |
| `server.key` | Clave privada del broker                             |

Comprobar el certificado que presenta el broker:

```bash
openssl s_client -connect localhost:8883 -CAfile certs/ca.crt -servername localhost
# Debe terminar con: Verify return code: 0 (ok)
```

Para conectar MQTT Explorer / MQTTX por TLS: host `localhost`, puerto `8883`, activar SSL/TLS y seleccionar `certs/ca.crt` como certificado CA.

> El puerto 1883 se mantiene abierto para el laboratorio; en producción se cerraría y solo se expondría 8883.

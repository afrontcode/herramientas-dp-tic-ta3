## TA Semana 10 - Grupo 4 - Simulación de sensor DHT-22

### 1. Crear y activar entorno virtual (Windows)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar dependencias

```powershell
python -m pip install --upgrade pip (opcional)
python -m pip install paho-mqtt
```

### 3. Correr la aplicación (solo si el servidor MQTT se encuentra activo)

```powershell
python sensor.py
```
# 🐺 Wolf-Byte Showcase

Página web de presentación y bot de demostración para Wolf-Byte - Soluciones de Inteligencia Artificial v1.0.

## 📁 Estructura del Proyecto

```
wolf-byte-showcase/
├── index.html              # Página web principal
├── assets/
│   ├── css/style.css      # Estilos minimalistas
│   └── img/               # Logo y recursos visuales
├── demo_bot.py            # Bot de demostración de Telegram
├── requirements.txt       # Dependencias de Python
├── .env                   # Variables de entorno
└── README.md             # Este archivo
```

## 🌐 Sitio Web

**URL:** https://eduardoge13.github.io/wolf-byte-showcase/

### Características:
- Diseño minimalista con tema blanco/invierno
- Logo estilizado con contenedor asimétrico
- Totalmente responsive
- 100% en español
- 3 paquetes de servicios destacados

### Paquetes:
1. **Paquete Lobo** - Análisis de Datos e Inteligencia de Negocios
2. **Paquete León** - Asistentes Virtuales Multicanal
3. **Paquete Dragón** - Agentes de IA Avanzados

## 🤖 Bot de Demostración

El bot muestra ejemplos interactivos de diferentes tipos de bots que se pueden crear.

### Comandos disponibles:
- `/start` - Menú principal con botones interactivos
- `/demo_datos` - Ejemplo de bot de análisis de datos
- `/demo_asistente` - Ejemplo de asistente virtual
- `/demo_ia` - Ejemplo de agente de IA
- `/ejemplos` - Casos de uso reales
- `/info` - Información sobre Wolf-Byte

##  Configuración Rápida

### 1. Crear Bot en Telegram

```bash
# 1. Buscar @BotFather en Telegram
# 2. Ejecutar: /newbot
# 3. Seguir instrucciones y guardar el TOKEN
```

### 2. Configurar Variables de Entorno

Crear archivo `.env`:

```bash
DEMO_BOT_TOKEN=tu_token_de_botfather
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar Bot Localmente

```bash
python demo_bot.py
```

### 5. Actualizar Link en la Página

En `index.html`, buscar y reemplazar:

```html
<!-- Antes -->
<a href="#" id="telegram-bot-link" ... style="opacity: 0.6;">
    Próximamente: Bot de Demo
</a>

<!-- Después -->
<a href="https://t.me/TU_BOT_USERNAME" target="_blank" class="contact-button primary">
    <i data-lucide="message-circle" class="button-icon"></i>
    Probar Bot en Telegram
</a>
```

## Despliegue en Google Cloud Run

### Prerrequisitos:
- Cuenta de Google Cloud Platform
- gcloud CLI instalado
- Proyecto GCP creado

### Pasos:

1. **Crear Dockerfile** (ya existe en el proyecto principal):

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY demo_bot.py .
CMD ["python", "demo_bot.py"]
```

2. **Configurar Secret Manager**:

```bash
# Guardar el token en Secret Manager
echo -n "TU_TOKEN_AQUI" | gcloud secrets create demo-bot-token --data-file=-

# Dar permisos a Cloud Run
gcloud secrets add-iam-policy-binding demo-bot-token \
    --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor"
```

3. **Deploy a Cloud Run**:

```bash
# Build y deploy
gcloud run deploy wolf-byte-demo-bot \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --set-secrets=DEMO_BOT_TOKEN=demo-bot-token:latest \
    --memory 512Mi \
    --timeout 300
```

4. **Verificar**:

```bash
# El bot debería estar corriendo 24/7
# Pruébalo en Telegram con /start
```

## Arquitectura

```
┌─────────────────────────────────────┐
│  GitHub Pages                       │
│  (Sitio Web Estático)               │
│  https://eduardoge13.github.io/...  │
└──────────────┬──────────────────────┘
               │
               │ Link al bot
               ▼
┌─────────────────────────────────────┐
│  Telegram                           │
│  (Mensajería)                       │
└──────────────┬──────────────────────┘
               │
               │ Webhook/Polling
               ▼
┌─────────────────────────────────────┐
│  Google Cloud Run                   │
│  (Bot Python 24/7)                  │
│  - demo_bot.py                      │
│  - Secret Manager (token)           │
└─────────────────────────────────────┘
```
### Para producción:
- Usar **Google Secret Manager** para tokens
- Activar **Cloud Armor** para protección DDoS
- Configurar **alertas de monitoreo**


## 📝 Proximamente version 2.0

- [ ] Desplegar bot a Google Cloud Run
- [ ] Actualizar link en index.html
- [ ] Agregar analytics a la página
- [ ] Configurar dominio personalizado

## 📧 Contacto

- **Email:** eduardo.gaitan.es@gmail.com
- **Sitio Web:** https://eduardoge13.github.io/wolf-byte-showcase/

## 📄 Licencia

Proyecto privado - Wolf-Byte © 2025

# Wolf-Byte Showcase Site

🐺 **El Invierno de los Datos Ha Llegado**

Sitio web estático de presentación para Wolf-Byte, inspirado en Game of Thrones, mostrando soluciones de IA y Ciencia de Datos.

## 🎯 Contenido

El sitio presenta 3 soluciones principales:

### 1. Casa Stark - Análisis de Datos End-to-End
- Análisis exploratorio profundo
- Modelos predictivos y proyecciones
- Dashboards interactivos
- Optimización de procesos

### 2. Casa Lannister - Chatbots Inteligentes
- Atención al cliente automatizada
- Consultas de base de datos
- Agendamiento automático
- Integración con WhatsApp/Telegram

### 3. Casa Targaryen - Agentes de IA Conversacional
- Comprensión de lenguaje natural
- Personalidad configurable
- Multilenguaje
- Integración con sistemas existentes

## 🚀 Deployment en GCP

### Opción 1: Cloud Storage (Sitio Estático) - Recomendado

```bash
# 1. Crear bucket en GCP
gsutil mb -p <PROJECT_ID> gs://wolf-byte-showcase

# 2. Configurar bucket para sitio web
gsutil web set -m index.html -e index.html gs://wolf-byte-showcase

# 3. Hacer bucket público
gsutil iam ch allUsers:objectViewer gs://wolf-byte-showcase

# 4. Subir archivos
cd /Users/eduardogaitan/Documents/projects/wolf-byte-showcase
gsutil -m cp -r * gs://wolf-byte-showcase/

# 5. Acceder al sitio
echo "https://storage.googleapis.com/wolf-byte-showcase/index.html"
```

### Opción 2: Cloud Storage + Load Balancer (Dominio Personalizado)

```bash
# 1. Crear bucket con nombre del dominio
gsutil mb -p <PROJECT_ID> gs://www.wolf-byte.com

# 2. Configurar bucket
gsutil web set -m index.html -e index.html gs://www.wolf-byte.com

# 3. Hacer público
gsutil iam ch allUsers:objectViewer gs://www.wolf-byte.com

# 4. Subir archivos
gsutil -m cp -r * gs://www.wolf-byte.com/

# 5. Configurar Load Balancer (usar consola GCP)
# - Backend: bucket de Cloud Storage
# - Frontend: IP externa
# - SSL: certificado managed de Google

# 6. Configurar DNS
# Apuntar dominio a la IP del Load Balancer
```

### Opción 3: Firebase Hosting (Más Simple)

```bash
# 1. Instalar Firebase CLI
npm install -g firebase-tools

# 2. Login
firebase login

# 3. Inicializar proyecto
cd /Users/eduardogaitan/Documents/projects/wolf-byte-showcase
firebase init hosting

# 4. Deploy
firebase deploy --only hosting

# 5. URL automática
# https://<project-id>.web.app
```

## 🛠️ Desarrollo Local

```bash
# Servidor simple con Python
cd /Users/eduardogaitan/Documents/projects/wolf-byte-showcase
python3 -m http.server 8080

# Abrir en navegador
open http://localhost:8080
```

## 📁 Estructura del Proyecto

```
wolf-byte-showcase/
├── index.html              # Página principal
├── assets/
│   ├── css/
│   │   └── style.css      # Estilos GoT theme
│   ├── js/
│   │   └── main.js        # Interactividad
│   └── img/
│       └── wolf-logo.svg  # Logo (opcional)
├── README.md              # Este archivo
└── deploy.sh              # Script de deployment
```

## 🎨 Características

- ✅ **Diseño Responsivo** - Funciona en móvil, tablet y desktop
- ✅ **Tema Game of Thrones** - Colores, tipografía y estilo medieval
- ✅ **Animaciones** - Efectos de scroll y transiciones suaves
- ✅ **Formulario de Contacto** - Captura de leads
- ✅ **Demos Interactivos** - Simulaciones de cada solución
- ✅ **SEO Optimizado** - Meta tags y estructura semántica
- ✅ **Performance** - Sitio estático ultra rápido

## 🎯 Personalización

### Cambiar Información de Contacto

Editar en `index.html` líneas 580-600:

```html
<div class="info-card">
    <div class="info-icon">📧</div>
    <h4>Email</h4>
    <p>tu-email@wolf-byte.com</p>
</div>
```

### Agregar Logo

1. Guardar logo como `assets/img/wolf-logo.svg`
2. El HTML ya tiene el elemento configurado

### Modificar Colores

Editar en `assets/css/style.css` líneas 1-20:

```css
:root {
    --lannister-gold: #d4af37;
    --ice-blue: #74b9ff;
    /* etc... */
}
```

## 🔗 URLs Útiles

- **GCP Console**: https://console.cloud.google.com
- **Cloud Storage**: https://console.cloud.google.com/storage
- **Firebase Console**: https://console.firebase.google.com

## 📊 Analytics (Opcional)

Agregar Google Analytics en `index.html` antes de `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

## 🚀 Quick Deploy

```bash
# Ejecutar script de deployment automático
chmod +x deploy.sh
./deploy.sh
```

## 📞 Soporte

Para preguntas o soporte, contacta a:
- Email: contacto@wolf-byte.com
- Telegram: @WolfByteBot

---

**"El Norte Recuerda... Tus Datos"**

*Wolf-Byte © 2025*

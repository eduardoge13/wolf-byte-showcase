# 🚀 Guía Rápida de Deployment

## ✅ Lo que se ha creado

Un sitio web estático profesional para Wolf-Byte con:

- ✨ **Diseño Game of Thrones** - Tema oscuro medieval con efectos visuales
- 📱 **Responsive** - Funciona en móvil, tablet y desktop
- 🎯 **3 Soluciones presentadas:**
  1. Análisis de Datos End-to-End (Casa Stark)
  2. Chatbots Inteligentes (Casa Lannister)
  3. Agentes de IA Conversacional (Casa Targaryen)
- 🎨 **Animaciones** - Scroll effects, typing indicators, charts
- 📧 **Formulario de contacto** - Listo para integrar con backend

## 🌐 Deployment en 3 Pasos

### Opción 1: Google Cloud Storage (Recomendado - Gratis)

```bash
cd /Users/eduardogaitan/Documents/projects/wolf-byte-showcase
./deploy.sh
```

El script te guiará por:
1. Login en GCP
2. Seleccionar proyecto
3. Crear bucket
4. Subir archivos
5. Te da URL pública

**Costo**: Gratis (bajo tráfico) o ~$0.026/GB almacenamiento

---

### Opción 2: Firebase Hosting (Súper Simple)

```bash
# 1. Instalar Firebase CLI
npm install -g firebase-tools

# 2. Login
firebase login

# 3. Ir al directorio
cd /Users/eduardogaitan/Documents/projects/wolf-byte-showcase

# 4. Inicializar (selecciona Hosting)
firebase init hosting

# 5. Deploy
firebase deploy --only hosting
```

Te da:
- URL: `https://tu-proyecto.web.app`
- SSL gratis
- CDN global
- CLI simple

**Costo**: Gratis (10GB storage, 360MB/día transferencia)

---

### Opción 3: Local Preview

```bash
# Ya está corriendo en:
open http://localhost:8080
```

## 🎨 Personalización Rápida

### Cambiar Información de Contacto

Edita `index.html` línea ~585:

```html
<p>tu-email@wolf-byte.com</p>
<p>+52 1 555-XXXX</p>
```

### Agregar Logo

1. Guarda tu logo como: `assets/img/wolf-logo.svg`
2. Ya está configurado en el HTML

### Cambiar Colores

Edita `assets/css/style.css` líneas 5-15:

```css
--lannister-gold: #d4af37;  /* Oro principal */
--ice-blue: #74b9ff;         /* Azul acento */
```

## 📊 Dominio Personalizado

### Con Firebase:

```bash
firebase hosting:channel:deploy production
# Luego en console: Settings > Add custom domain
```

### Con Cloud Storage + Load Balancer:

1. Console GCP → Load Balancing
2. Create Load Balancer → HTTP(S)
3. Backend: tu bucket de Cloud Storage
4. Frontend: Reserved IP + SSL certificate
5. DNS: Apuntar dominio a la IP

## 🔍 SEO y Analytics

### Google Analytics (opcional):

Agrega antes de `</head>` en `index.html`:

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Meta Tags (ya incluidos):

```html
<meta name="description" content="Wolf-Byte - Soluciones de IA y Ciencia de Datos">
<meta property="og:title" content="Wolf-Byte">
<meta property="og:description" content="El Invierno de los Datos Ha Llegado">
```

## 📱 Integración con tu Bot

Enlaza desde el sitio a tu bot de Telegram:

```html
<a href="https://t.me/tu_bot_username?start=demo">Prueba el Bot</a>
```

## 🎯 Para Clientes

**Comparte esta URL después del deployment:**

```
https://storage.googleapis.com/wolf-byte-showcase/index.html

o

https://tu-proyecto.web.app
```

## 💡 Tips para Presentaciones

1. **Live Demo**: Abre el sitio en una pestaña
2. **Scroll suave**: Muestra las 3 soluciones
3. **Formulario**: Demuestra el formulario de contacto
4. **Responsive**: Muestra en móvil también

## 🚨 Troubleshooting

### "Permission denied" al deployar:
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

### Bucket ya existe:
```bash
# Usa otro nombre o borra el existente
gsutil rm -r gs://wolf-byte-showcase
```

### Servidor local no inicia:
```bash
# Puerto ocupado? Usa otro
python3 -m http.server 9000
```

## 📞 Next Steps

1. ✅ Preview local: `http://localhost:8080`
2. ✅ Deploy a GCP: `./deploy.sh`
3. ✅ Compartir URL con clientes
4. 📧 Configurar form backend (opcional)
5. 🌐 Dominio personalizado (opcional)
6. 📊 Analytics (opcional)

---

**El sitio está listo para mostrar a clientes! 🎉**

"El Norte Recuerda... Tus Datos" 🐺

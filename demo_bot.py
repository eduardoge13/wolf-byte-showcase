#!/usr/bin/env python3
"""
Wolf-Byte Demo Bot - Bot de demostración simplificado
Muestra ejemplos de diferentes tipos de bots sin necesitar bases de datos
"""

import os
import logging
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Cargar variables de entorno
load_dotenv()

# Configuración de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Token del bot
BOT_TOKEN = os.getenv('DEMO_BOT_TOKEN') or os.getenv('TELEGRAM_BOT_TOKEN')

class WolfByteDemoBot:
    """Bot de demostración Wolf-Byte"""
    
    def __init__(self):
        if not BOT_TOKEN:
            raise ValueError("❌ No se encontró DEMO_BOT_TOKEN o TELEGRAM_BOT_TOKEN en .env")
        
        self.application = None
        logger.info("✅ Bot inicializado correctamente")
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Comando /start - Mensaje de bienvenida"""
        user = update.effective_user
        
        welcome_message = f"""🐺 **¡Hola {user.first_name}! Bienvenido a Wolf-Byte**

Soy un bot de demostración que muestra diferentes capacidades de IA.

📋 **Comandos disponibles:**

🔹 /datos - Ver ejemplo de análisis de datos
🔹 /asistente - Probar asistente virtual  
🔹 /agente - Conversar con agente de IA
🔹 /ejemplos - Casos de uso reales
🔹 /info - Información sobre Wolf-Byte

💬 También puedes escribirme cualquier mensaje y te responderé de forma inteligente.

¿Qué te gustaría probar?"""
        
        await update.message.reply_text(welcome_message, parse_mode='Markdown')
        logger.info(f"User {user.id} ({user.username}) started the bot")
    
    async def datos_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Demo de bot de análisis de datos"""
        message = """📊 **DEMO: Bot de Datos e Inteligencia de Negocios**

Este tipo de bot puede:
✅ Consultar bases de datos en tiempo real
✅ Generar reportes automáticos
✅ Crear dashboards interactivos
✅ Análisis predictivo

**Ejemplo de consulta:**

👤 Usuario: "¿Cuántas ventas tuvimos hoy?"

🤖 Bot:
```
📈 Reporte de Ventas - Hoy
• Total ventas: $45,230 MXN
• Transacciones: 23
• Ticket promedio: $1,966 MXN
• Producto top: Paquete Premium (8)

📊 vs Ayer: +15% 📈
```

💼 **Casos de uso:**
• E-commerce
• Restaurantes
• Retail
• Servicios

¿Te interesa? Escríbeme a: eduardo.gaitan.es@gmail.com"""
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def asistente_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Demo de asistente virtual"""
        message = """💬 **DEMO: Asistente Virtual Multicanal**

Este tipo de bot puede:
✅ Atender clientes 24/7
✅ Responder preguntas frecuentes
✅ Procesar pedidos y reservas
✅ Integración WhatsApp/Telegram/Web

**Ejemplo de conversación:**

👤: "¿Horario de atención?"
🤖: Lun-Vie 9:00-18:00 hrs

👤: "Quiero una reserva"
🤖: ¡Perfecto! ¿Para cuántas personas?

👤: "4 personas"
🤖: ¿Qué día prefieres?

👤: "Mañana 2pm"
🤖: ✅ Reserva confirmada
• Fecha: Mañana 14:00
• Personas: 4
• #RES2024-001

💼 **Casos de uso:**
• Restaurantes
• Clínicas
• Hoteles
• Soporte técnico

Contacto: eduardo.gaitan.es@gmail.com"""
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def agente_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Demo de agente de IA"""
        message = """🤖 **DEMO: Agente de IA con Lenguaje Natural**

Este tipo de bot puede:
✅ Entender lenguaje natural
✅ Mantener contexto de conversación
✅ Respuestas personalizadas
✅ Aprendizaje continuo

**Ejemplo de conversación:**

👤: "Hola, busco solución para mi negocio"

🤖: ¡Hola! Me encantaría ayudarte. ¿Qué tipo de negocio tienes?

👤: "Una cafetería, necesito controlar inventario"

🤖: Entiendo. Para una cafetería, te recomiendo el **Paquete Lobo** que incluye:

📊 Inventario en tiempo real
📈 Predicción de demanda
🔔 Alertas de stock bajo
📱 Acceso móvil

¿Te gustaría una demo personalizada?

💼 **Casos de uso:**
• Consultoría automatizada
• Ventas conversacionales
• Onboarding de clientes
• Soporte especializado

Contacto: eduardo.gaitan.es@gmail.com"""
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def ejemplos_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Mostrar ejemplos de uso"""
        message = """📖 **Ejemplos de Casos de Uso**

🏪 **E-commerce**
Bot que procesa pedidos, responde sobre productos y envía confirmaciones

🏥 **Clínica Médica**
Asistente que agenda citas, envía recordatorios y responde FAQ

🍕 **Restaurante**
Bot de pedidos con menú, seguimiento de entrega y pagos

📚 **Escuela**
Sistema de consultas de calificaciones, horarios y avisos

💼 **Empresa B2B**
Reportes de ventas, análisis de clientes y pronósticos

🏋️ **Gimnasio**
Gestión de membresías, horarios y planes personalizados

**Todos incluyen:**
✨ Integración con bases de datos
✨ Pagos automáticos
✨ Reportes y análisis
✨ Multilenguaje
✨ Escalabilidad ilimitada

🌐 **Sitio web:**
https://eduardoge13.github.io/wolf-byte-showcase/

📧 **Contacto:**
eduardo.gaitan.es@gmail.com"""
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def info_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Información sobre Wolf-Byte"""
        message = """🐺 **Wolf-Byte - Soluciones de IA**

Creamos bots y sistemas de IA personalizados.

📦 **Nuestros Paquetes:**

**🐺 Paquete Lobo**
Análisis de Datos e Inteligencia de Negocios
• Dashboards en tiempo real
• Modelos predictivos
• Reportes automáticos

**🦁 Paquete León**
Asistentes Virtuales Multicanal
• Atención 24/7
• WhatsApp/Telegram
• Integración con sistemas

**🐉 Paquete Dragón**
Agentes de IA Avanzados
• Procesamiento de lenguaje natural
• Conversaciones contextuales
• Aprendizaje continuo

🌐 **Sitio Web:**
https://eduardoge13.github.io/wolf-byte-showcase/

📧 **Contacto:**
eduardo.gaitan.es@gmail.com

💼 **¿Listo para transformar tu negocio?**
Escríbeme y platicamos sobre tu proyecto."""
        
        await update.message.reply_text(message, parse_mode='Markdown')
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Manejar mensajes de texto"""
        user_message = update.message.text.lower()
        user = update.effective_user
        
        logger.info(f"Message from {user.id} ({user.username}): {update.message.text}")
        
        # Respuestas inteligentes basadas en palabras clave
        if any(word in user_message for word in ['hola', 'hey', 'buenas', 'hi']):
            response = f"¡Hola {user.first_name}! 👋\n\nUsa /start para ver todo lo que puedo hacer."
        
        elif any(word in user_message for word in ['precio', 'costo', 'cuanto', 'cuánto']):
            response = """💰 **Precios personalizados**

Los costos varían según tus necesidades específicas.

Contáctame para una cotización personalizada:
📧 eduardo.gaitan.es@gmail.com

O visita:
🌐 https://eduardoge13.github.io/wolf-byte-showcase/"""
        
        elif any(word in user_message for word in ['ayuda', 'help', 'comandos']):
            response = """📋 **Comandos disponibles:**

/start - Menú principal
/datos - Demo de bot de datos
/asistente - Demo de asistente
/agente - Demo de IA
/ejemplos - Casos de uso
/info - Info de Wolf-Byte"""
        
        elif any(word in user_message for word in ['gracias', 'thanks', 'ok']):
            response = "¡De nada! 😊 Si necesitas algo más, aquí estoy."
        
        else:
            response = f"""🤔 Interesante pregunta, {user.first_name}.

Este es un bot de demostración. Te puedo mostrar:

📊 /datos - Análisis de datos
💬 /asistente - Asistentes virtuales
🤖 /agente - Agentes de IA
📖 /ejemplos - Casos de uso

O escríbeme directamente:
📧 eduardo.gaitan.es@gmail.com"""
        
        await update.message.reply_text(response, parse_mode='Markdown')
    
    def run(self):
        """Iniciar el bot"""
        try:
            # Crear aplicación
            self.application = Application.builder().token(BOT_TOKEN).build()
            
            # Agregar handlers
            self.application.add_handler(CommandHandler("start", self.start_command))
            self.application.add_handler(CommandHandler("datos", self.datos_command))
            self.application.add_handler(CommandHandler("asistente", self.asistente_command))
            self.application.add_handler(CommandHandler("agente", self.agente_command))
            self.application.add_handler(CommandHandler("ejemplos", self.ejemplos_command))
            self.application.add_handler(CommandHandler("info", self.info_command))
            self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
            
            # Iniciar bot
            logger.info("🐺 Wolf-Byte Demo Bot iniciado - Esperando mensajes...")
            logger.info("📋 Comandos: /start /datos /asistente /agente /ejemplos /info")
            self.application.run_polling(drop_pending_updates=True)
            
        except KeyboardInterrupt:
            logger.info("🛑 Bot detenido por el usuario")
        except Exception as e:
            logger.error(f"❌ Error crítico: {e}")
            raise

if __name__ == '__main__':
    bot = WolfByteDemoBot()
    bot.run()

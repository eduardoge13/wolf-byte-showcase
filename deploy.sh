#!/bin/bash

# Wolf-Byte Showcase Deployment Script
# Deploy static site to Google Cloud Storage

set -e

echo "🐺 Wolf-Byte Showcase Deployment"
echo "================================"
echo ""

# Configuration
PROJECT_ID=""
BUCKET_NAME="wolf-byte-showcase"
REGION="us-central1"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo -e "${RED}❌ gcloud CLI no está instalado${NC}"
    echo "Instala desde: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Check if logged in
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" &> /dev/null; then
    echo -e "${YELLOW}⚠️  No estás logueado en gcloud${NC}"
    echo "Ejecutando login..."
    gcloud auth login
fi

# Get current project or ask for one
CURRENT_PROJECT=$(gcloud config get-value project 2>/dev/null)

if [ -z "$CURRENT_PROJECT" ]; then
    echo -e "${YELLOW}📋 Proyectos disponibles:${NC}"
    gcloud projects list
    echo ""
    read -p "Ingresa el PROJECT_ID a usar: " PROJECT_ID
    gcloud config set project $PROJECT_ID
else
    echo -e "${GREEN}✓ Proyecto actual: $CURRENT_PROJECT${NC}"
    read -p "¿Usar este proyecto? (y/n): " USE_CURRENT
    if [ "$USE_CURRENT" != "y" ]; then
        read -p "Ingresa el PROJECT_ID a usar: " PROJECT_ID
        gcloud config set project $PROJECT_ID
    else
        PROJECT_ID=$CURRENT_PROJECT
    fi
fi

echo ""
echo "🚀 Configuración:"
echo "  - Proyecto: $PROJECT_ID"
echo "  - Bucket: $BUCKET_NAME"
echo "  - Región: $REGION"
echo ""

read -p "¿Continuar con deployment? (y/n): " CONTINUE
if [ "$CONTINUE" != "y" ]; then
    echo "Deployment cancelado"
    exit 0
fi

echo ""
echo "📦 Step 1: Verificando bucket..."

# Check if bucket exists
if gsutil ls -b gs://$BUCKET_NAME &> /dev/null; then
    echo -e "${GREEN}✓ Bucket ya existe${NC}"
else
    echo "Creando bucket..."
    gsutil mb -p $PROJECT_ID -l $REGION gs://$BUCKET_NAME
    echo -e "${GREEN}✓ Bucket creado${NC}"
fi

echo ""
echo "🌐 Step 2: Configurando bucket para sitio web..."
gsutil web set -m index.html -e index.html gs://$BUCKET_NAME

echo ""
echo "🔓 Step 3: Haciendo bucket público..."
gsutil iam ch allUsers:objectViewer gs://$BUCKET_NAME

echo ""
echo "📤 Step 4: Subiendo archivos..."

# Set cache control for different file types
echo "  Subiendo HTML..."
gsutil -m -h "Cache-Control:public, max-age=3600" cp -r *.html gs://$BUCKET_NAME/

echo "  Subiendo CSS..."
gsutil -m -h "Cache-Control:public, max-age=86400" cp -r assets/css/* gs://$BUCKET_NAME/assets/css/

echo "  Subiendo JavaScript..."
gsutil -m -h "Cache-Control:public, max-age=86400" cp -r assets/js/* gs://$BUCKET_NAME/assets/js/

echo "  Subiendo imágenes..."
if [ -d "assets/img" ] && [ "$(ls -A assets/img)" ]; then
    gsutil -m -h "Cache-Control:public, max-age=604800" cp -r assets/img/* gs://$BUCKET_NAME/assets/img/
fi

echo ""
echo -e "${GREEN}✅ Deployment completado!${NC}"
echo ""
echo "🌐 URLs de acceso:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  📍 URL Pública:"
echo "     https://storage.googleapis.com/$BUCKET_NAME/index.html"
echo ""
echo "  📍 URL Cloud Storage:"
echo "     https://$BUCKET_NAME.storage.googleapis.com/index.html"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "💡 Próximos pasos:"
echo ""
echo "  1. Configurar dominio personalizado:"
echo "     - Crear CNAME: www.wolf-byte.com -> c.storage.googleapis.com"
echo "     - Crear bucket: gs://www.wolf-byte.com"
echo "     - Re-deploy a ese bucket"
echo ""
echo "  2. Agregar SSL con Load Balancer:"
echo "     - Console: https://console.cloud.google.com/net-services/loadbalancing"
echo "     - Backend: bucket de Cloud Storage"
echo "     - Frontend: IP + SSL certificate"
echo ""
echo "  3. Agregar CDN para mejor performance:"
echo "     - Habilitar Cloud CDN en Load Balancer"
echo ""
echo "🐺 El Norte Recuerda... Tus Datos!"
echo ""

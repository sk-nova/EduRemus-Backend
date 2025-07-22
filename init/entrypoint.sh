#!/bin/sh

# 💥 Exit immediately on any error
set -e

# ────────────────────────────────────────────────────────────────
# 🎨 Color definitions for styled terminal output
# ────────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color (reset)


# 📦 Function to wait for a database to be available
wait_for_db() {
    echo "⏳${BLUE} Waiting for $1 at $2:$3...${NC}"

    while ! nc -z "$2" "$3"; do
        sleep 0.1
    done

    echo "✅${GREEN}  $1 is up and running!${NC}"
}


# ────────────────────────────────────────────────────────────────
# 📡 Wait for Database to become ready
# ────────────────────────────────────────────────────────────────
echo "${BLUE}📡 Waiting for "$DATABASE" to be ready...${NC}"


# 🗄️ Handle database readiness based on DATABASE environment variable
case "$DATABASE" in
    postgres)
        wait_for_db "🐘 PostgreSQL" "$POSTGRES_HOST" "$POSTGRES_PORT"
        ;;
    mysql)
        wait_for_db "🦊 MySQL" "$MYSQL_HOST" "$MYSQL_PORT"
        ;;
    *)
        echo -e "⚠️${RED} Skipping database wait – unknown or unset DATABASE: '$DATABASE'${NC}"
        ;;
esac


# 📁 Navigate to Django project directory
echo "📂 ${BLUE}Moving into project directory...${NC}"

cd src/

# 🧹 Clear the database in testing environment (⚠️ use with caution)
if [ "$DJANGO_ENV" = "testing" ]; then
    echo -e "${BLUE}🧹 Cleaning the database...${NC}"
    
    python manage.py flush --no-input
fi


# 🔧 Apply migrations
echo "🔄 ${BLUE}Applying database migrations...${NC}"

python manage.py migrate


# ────────────────────────────────────────────────────────────────
# 🎯 (Optional) Collect static files
# ────────────────────────────────────────────────────────────────
# echo "📦 ${BLUE}Collecting static files...${NC}"
# python manage.py collectstatic --no-input


# ────────────────────────────────────────────────────────────────
# 👤 (Optional) Create a Django superuser
# ────────────────────────────────────────────────────────────────
if [ "$CREATE_SUPERUSER" = "true" ]; then
  echo "${BLUE}👤 Creating superuser...${NC}"
  python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists():
    User.objects.create_superuser(
        username='${DJANGO_SUPERUSER_USERNAME}',
        email='${DJANGO_SUPERUSER_EMAIL}',
        password='${DJANGO_SUPERUSER_PASSWORD}'
    )
END
fi


# ────────────────────────────────────────────────────────────────
# 📥 (Optional) Load initial fixtures into the database
# ────────────────────────────────────────────────────────────────
if [ "$LOAD_FIXTURES" = "true" ]; then
  echo "${BLUE}📥 Loading fixtures...${NC}"
  python manage.py loaddata initial_data.json
fi


# ────────────────────────────────────────────────────────────────
# 🚀 Launch Django dev server with Werkzeug debugger
# ────────────────────────────────────────────────────────────────
echo "🌐 ${GREEN}Starting Django development server at http://0.0.0.0:8000 ...${NC}"

python manage.py runserver_plus 0.0.0.0:8000

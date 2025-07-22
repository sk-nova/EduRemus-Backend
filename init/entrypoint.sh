#!/bin/sh

# 💥 Exit immediately on any error
set -e


# 📦 Function to wait for a database to be available
wait_for_db() {
    echo "⏳ Waiting for $1 at $2:$3..."

    while ! nc -z "$2" "$3"; do
        sleep 0.1
    done

    echo "✅ $1 is up and running!"
}


# 🗄️ Handle database readiness based on DATABASE environment variable
case "$DATABASE" in
    postgres)
        wait_for_db "🐘 PostgreSQL" "$POSTGRES_HOST" "$POSTGRES_PORT"
        ;;
    mysql)
        wait_for_db "🦊 MySQL" "$MYSQL_HOST" "$MYSQL_PORT"
        ;;
    *)
        echo "⚠️ Skipping database wait – unknown or unset DATABASE: '$DATABASE'"
        ;;
esac


# 📁 Navigate to Django project directory
echo -n "📂 Moving into project directory..."

ls

cd src/

# 🧹 Optional: Reset the database (DANGER in production!)
# echo "⚠️ Flushing the database..."
# python manage.py flush --no-input


# 🔧 Apply migrations
echo "🔄 Applying database migrations..."

python manage.py migrate


# 🎨 Collect static files (optional for production)
# echo "📦 Collecting static files..."
# python manage.py collectstatic --no-input


# 🚀 Launch Django dev server with Werkzeug debugger
echo "🌐 Starting Django development server at http://0.0.0.0:8000 ..."

python manage.py runserver_plus 0.0.0.0:8000

Comando para encender entorno virtual
source venv/bin/activate

Instalar dependenciar

# Producción

pip install -r requirements.txt

# Desarrollo

pip install -r requirements-dev.txt

#Iniciar servidor de postgresql en local

Primero ver sí está instlado
psql --version

Si dice command not found, debes instalarlo,
brew install postgresql

Iniciar el servidor PostgreSQL
brew services start postgresql

Crear la base de datos
psql -U elgalileo -d template1

Y ahí puedes crear tu base de datos local con
CREATE DATABASE postgres_local;

Luego saler con \q e ingresas con el siguiente comando
psql -h localhost postgres_local

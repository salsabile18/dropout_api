FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

# Copier le script de démarrage dans le conteneur
COPY start.sh .

# Exposer les ports 8000, 8001 et 8002
EXPOSE 8000
EXPOSE 8001
EXPOSE 8002

# Définir le script de démarrage comme commande par défaut
CMD ["./start.sh"]

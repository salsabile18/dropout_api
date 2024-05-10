# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

# Exposition du port 8000 utilisé par l'application
EXPOSE 8000
EXPOSE 8001
EXPOSE 8002

# Commande pour exécuter l'application lorsqu'un conteneur basé sur cette image est démarré
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# Utiliser l'image Python 3.8
FROM python:3.8

# Définir le répertoire de travail dans l'image
WORKDIR /GIT

# Copier le fichier requirements.txt du répertoire local dans l'image
COPY ./requirements.txt /GIT/requirements.txt

# Installer les dépendances Python spécifiées dans le fichier requirements.txt
RUN pip install --no-cache-dir --upgrade -r /GIT/requirements.txt

# Copier le contenu du répertoire local dans l'image
COPY ./app /GIT/app

# Définir la commande par défaut à exécuter lorsque le conteneur démarre
CMD ["uvicorn", "app.myfastapi:app", "--host", "0.0.0.0", "--port", "8080"]
# Comment excuter le projet
1 - Clonez le projet depuis github


# Lancez le backend 


2 - Assurez-vous que vous avez python installé sur votre poste

3 - Ouvrez un terminal ou votre invite de commande

4 - Créez votre environnement virtuel

5 - Activez votre enrironnement virtuel

6 - Installez les dépendances en tapant la commande ci-dessous
```
 pip install -r requirements.txt
```

7 - Assurez-vous que vous avez postgresql installé sur votre poste

8 - Créez une base de données postgresql

9 - Connectez la base de données au backend
    Pour ce faire:
    a - Allez-y dans To-Do-List/backend/config/settings.py
    b - Remplacez ces informations :

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'NomDeVotreBaseDeDonnées',
                'USER': 'LeNomD'utilisateur',
                'PASSWORD': 'LeMotDePasseDeVotreUtilisateur',
                'HOST': 'localhost',
                'PORT': 'LePortQueVousAvezDeL'installationDePostgresql',
            }
        }

10 - Faites les migrations en tapant les commandes ci-dessous
```
 python manage.py makemigrations
 python manage.py migrate
```

11 - Lancez le serveur en tapant la commande ci-dessous
```
 python manage.py runserver
```

POUR VOIR LA DOCUMENTATION DE L'API, TAPEZ :
```
 http://127.0.0.1:8000/swagger/
```

# Lancez le frontend 


1 - Assurez-vous que vous avez nodejs installé sur votre poste

2 - Assurez-vous que vous avez Vuejs installé sur votre poste

3 - Ouvrez un deuxième terminal ou invite de commande

4 - Placez vous dans le dossier To-Do-List/frontend

5 - Tapez la commande ci-dessous
```
 npm install
```

6 - lanez le serveur
```
 npm run serve
```


7 - Dans votre navigateur, tapez:
```
 http://localhost:8080/
```

### Compiles and minifies for production
```
npm run build
```
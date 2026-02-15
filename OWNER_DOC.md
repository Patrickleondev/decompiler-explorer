# 🚀 Guide d'Installation : Decompiler Explorer (Version Illimitée)

Bienvenue dans cette version personnalisée de **Decompiler Explorer**. Cet outil a été modifié pour supprimer les limites de taille d'upload (2MB -> 1GB) et désactiver les brides de performance (throttling), ce qui en fait un allié parfait pour le Reverse Engineering et les CTFs.

---

## 📋 Pré-requis (Avant de commencer)

Assurez-vous d'avoir installé les logiciels suivants sur votre machine (Windows, Linux ou Kali) :

1.  **Git** : Pour télécharger le projet.
2.  **Docker Desktop** (si vous êtes sur Windows) ou **Docker Engine** (sur Linux).
3.  **Python** (Version 3.10 ou plus récente).
4.  **Connexion Internet** : Recommandée pour le premier téléchargement des images (elles sont volumineuses).

---

## 🛠️ Installation Étape par Étape

### 1. Télécharger (Cloner) le Projet
Ouvrez un terminal (CMD, PowerShell ou Terminal Linux) et tapez :
```bash
git clone https://github.com/Patrickleondev/decompiler-explorer.git
cd decompiler-explorer
```

### 2. Activer Docker Swarm
Ce projet utilise une technologie appelée "Swarm" pour gérer les décompilateurs. Vous devez l'activer une seule fois :
```bash
docker swarm init
```
*(Si vous recevez un message disant que Swarm est déjà actif, passez à l'étape suivante).*

### 3. Installer l'Environnement Python
Nous utilisons `pipenv` pour isoler les dépendances. Installez-le d'abord, puis configurez le projet :
```bash
pip install pipenv
pipenv install --python python3
```

### 4. Initialisation des Secrets
Cette commande crée les dossiers nécessaires et génère des clés de sécurité pour votre instance locale :
```bash
pipenv run python scripts/dce.py init
```

### 5. Construction des Images (Le "Build")
C'est l'étape la plus longue. Elle prépare les conteneurs Docker. 
*Note : Nous excluons certains décompilateurs lourds ici pour aller plus vite.*
```bash
pipenv run python scripts/dce.py --without-angr --without-binja --without-recstudio --without-reko --without-retdec --without-revng --without-snowman build
```

### 6. Lancement du Serveur
Lancez enfin l'outil :
```bash
pipenv run python scripts/dce.py start
```

---

## 🖥️ Comment accéder à l'outil (GUI)

L'interface graphique est accessible via votre navigateur web.
- **Ouvrez votre navigateur** (Chrome, Firefox, etc.).
- **Tapez l'adresse suivante** : `http://localhost`

Vous devriez voir l'interface de Decompiler Explorer prête à l'emploi !

---

## 🦸 Fonctionnalités de cette Version Custom

### 📦 Upload de gros fichiers
Contrairement à la version officielle limitée à 2MB, vous pouvez ici uploader des fichiers allant jusqu'à **1 Go**. 

### ⚡ Import de Challenges en Masse (CTF)
Si vous avez un dossier rempli de challenges (ex: 50 fichiers .exe), vous n'avez pas besoin de les uploader un par un :
1. Copiez vos fichiers dans un dossier du projet.
2. Lancez cette commande :
```bash
docker exec -it $(docker ps -qf "name=dogbolt_explorer") python manage.py import_ctf /chemin/vers/votre/dossier
```

### 🔓 Pas de limite de vitesse
Les restrictions de "Rate Limiting" (qui vous bloquent si vous faites trop de requêtes) ont été supprimées pour un usage local fluide.

---

## ❓ En cas de problème

- **Port 80 déjà utilisé** : Si vous avez un autre service web lancé (comme Apache ou Nginx), le démarrage échouera. Arrêtez les autres services ou changez le port dans `docker-compose.yml`.
- **Espace Disque** : Ghidra et les autres décompilateurs prennent beaucoup de place. Prévoyez au moins 10-20 Go d'espace libre.
- **Python-version** : Si `pipenv` se plaint de la version de Python, vérifiez que vous avez Python 3.10 ou supérieur installé.

---
*Documentation générée pour la version personnalisée de Decompiler Explorer.*

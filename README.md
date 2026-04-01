#  CyberScan

CyberScan est un outil de cybersécurité développé en Python permettant d’analyser automatiquement la surface d’attaque d’un site web.

Il simule le comportement d’un pentester en effectuant plusieurs types de scans afin de détecter des faiblesses potentielles.

---

##  Fonctionnalités

*  Analyse des headers de sécurité
*  Détection de pages sensibles (`/admin`, `/login`, etc.)
*  Analyse des formulaires (login, méthode, inputs)
*  Crawler (exploration automatique du site)
*  Multithreading (scan rapide)
*  Génération de rapport JSON
*  Détection des technologies (serveur, backend, CMS)

---

##  Objectif

CyberScan permet de :

* Automatiser la reconnaissance d’un site web
* Identifier des mauvaises configurations de sécurité
* Comprendre la surface d’attaque d’une application web

---

##  Installation

### 1. Cloner le projet

```bash
git clone https://github.com/tonpseudo/cyberscan.git
cd cyberscan
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
```

### 3. Activer l’environnement

* Windows :

```bash
venv\Scripts\activate
```

* Linux / Mac :

```bash
source venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

##  Utilisation

Lancer le programme :

```bash
python main.py
```

Entrer l’URL cible :

```bash
Cible (URL): https://example.com
```

---

##  Exemple de résultat

###  Console

```
===== Scan de : https://example.com =====

Analyse des headers de sécurité :
[!] Content-Security-Policy manquant
[OK] X-Frame-Options présent

Scan des pages sensibles :
[!!] Page trouvée : /admin

Analyse des formulaires :
[INFO] Formulaire de login détecté 
```

---

### 📄 Rapport JSON

```json
{
  "url": "https://example.com",
  "data": {
    "headers": {
      "Content-Security-Policy": false,
      "X-Frame-Options": true
    },
    "pages": [
      {
        "url": "https://example.com/admin",
        "status": 200
      }
    ],
    "forms": [
      {
        "action": "login.php",
        "method": "POST",
        "inputs": [
          {
            "name": "username",
            "type": "text"
          }
        ]
      }
    ]
  }
}
```

---

## Auteur

Projet réalisé par KONGO MITOUMBA Olivier dans le cadre d’un apprentissage en cybersécurité.

---

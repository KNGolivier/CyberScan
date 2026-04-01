import requests
import urllib3

# Désactiver les warnings SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get(url):
    try:
        response = requests.get(
            url,
            timeout=5,
            verify=False  # Désactive la vérification SSL
        )
        return response
    except requests.exceptions.RequestException as e:
        print(f"[ERREUR] {e}")
        return None
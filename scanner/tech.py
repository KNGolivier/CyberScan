from core.requester import get

def detect_technologies(url):
    response = get(url)

    if not response:
        return None

    headers = response.headers
    tech = {}

    # Serveur
    server = headers.get("Server")
    if server:
        tech["server"] = server

    # Technologie backend
    powered_by = headers.get("X-Powered-By")
    if powered_by:
        tech["backend"] = powered_by

    # Détection simple via contenu
    content = response.text.lower()

    if "wp-content" in content:
        tech["cms"] = "WordPress"

    if "laravel" in content:
        tech["framework"] = "Laravel"

    if "django" in content:
        tech["framework"] = "Django"

    return tech
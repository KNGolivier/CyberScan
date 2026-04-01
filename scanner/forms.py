from core.requester import get
from bs4 import BeautifulSoup

def scan_forms(url):
    response = get(url)

    if not response:
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")

    results = []

    for form in forms:
        action = form.get("action")
        method = form.get("method", "GET").upper()

        form_data = {
            "action": action,
            "method": method,
            "inputs": []
        }

        inputs = form.find_all("input")

        for inp in inputs:
            form_data["inputs"].append({
                "name": inp.get("name"),
                "type": inp.get("type")
            })

        results.append(form_data)

    return results
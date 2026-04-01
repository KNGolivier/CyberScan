from core.requester import get

def scan_pages(url):
    paths = [
        "/admin",
        "/login",
        "/backup",
        "/.env",
        "/config",
        "/dashboard"
    ]

    print("\nScan des pages sensibles :\n")

    for path in paths:
        full_url = url.rstrip("/") + path
        response = get(full_url)

        if response:
            status = response.status_code

            if status == 200:
                print(f"[!!] Page trouvée : {full_url}")
            elif status in [301, 302]:
                print(f"[→] Redirection : {full_url}")
            else:
                print(f"[--] {full_url} ({status})")
        else:
            print(f"[XX] Erreur : {full_url}")
from core.requester import get

def check_headers(url):
    response = get(url)

    if not response:
        return None

    headers = response.headers

    results = {}

    security_headers = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "Strict-Transport-Security",
        "X-Content-Type-Options"
    ]

    for header in security_headers:
        results[header] = header in headers

    return results
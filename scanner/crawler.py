from core.requester import get
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()

def crawl(url):
    print("\n[CRAWLER] Exploration du site...\n")

    to_visit = [url]

    while to_visit:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        print(f"[+] Visite : {current_url}")
        visited.add(current_url)

        response = get(current_url)

        if not response:
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")

            if href:
                full_url = urljoin(url, href)

                # garder seulement les liens internes
                if urlparse(full_url).netloc == urlparse(url).netloc:
                    if full_url not in visited:
                        to_visit.append(full_url)

    return visited
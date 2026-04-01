from scanner.headers import check_headers
from scanner.pages import scan_pages
from scanner.forms import scan_forms
from scanner.crawler import crawl
from scanner.tech import detect_technologies

from utils.report import add_result, save_report
from concurrent.futures import ThreadPoolExecutor

target = input("Cible (URL): ")

urls = crawl(target)

def scan_target(url):
    print(f"\n===== Scan de : {url} =====")

   
    data = {}

    data["headers"] = check_headers(url)
    data["pages"] = scan_pages(url)
    data["forms"] = scan_forms(url)
    data["technologies"] = detect_technologies(url)

    add_result(url, data)

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(scan_target, urls)

save_report()
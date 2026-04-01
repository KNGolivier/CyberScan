import json

report_data = []

def add_result(url, data):
    report_data.append({
        "url": url,
        "data": data
    })

def save_report(filename="report.json"):
    with open(filename, "w") as f:
        json.dump(report_data, f, indent=4)

    print(f"\n[✔] Rapport sauvegardé dans {filename}")
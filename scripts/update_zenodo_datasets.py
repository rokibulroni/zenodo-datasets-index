import requests
import json
import os

ZENODO_API = "https://zenodo.org/api/records?q=cybersecurity+phishing+malware+ransomware+hacking+forensic+pentest+ids+ips+siem+zeroday+exploit+ddos+threat+mitre+nmap+network+firewall+vulnerability+reverse+osint+incident+log+password+encryption+soc+mitigation+cybercrime+cti+breach+suricata+yara+wireshark+anomaly+dfir+cyberattack&type=dataset&size=300"

try:
    response = requests.get(ZENODO_API)
    data = response.json()

    datasets = []

    for item in data.get("hits", {}).get("hits", []):
        meta = item.get("metadata", {})
        dataset = {
            "id": item.get("id"),
            "title": meta.get("title", ""),
            "description": meta.get("description", "")[:300],
            "url": item.get("links", {}).get("html"),
            "doi": meta.get("doi", ""),
            "keywords": meta.get("keywords", []),
            "published": meta.get("publication_date", ""),
            "creators": [c.get("name") for c in meta.get("creators", [])]
        }
        datasets.append(dataset)

    os.makedirs("data", exist_ok=True)
    with open("data/zenodo_datasets.json", "w") as f:
        json.dump(datasets, f, indent=2)

    print(f"✅ Saved {len(datasets)} datasets to data/zenodo_datasets.json")

except Exception as e:
    print("❌ Error:", str(e))


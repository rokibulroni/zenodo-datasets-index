

# 🛡️ Zenodo Cybersecurity Datasets Index

This repository automatically fetches and updates a list of **300+ cybersecurity-related open datasets** from [Zenodo.org](https://zenodo.org/), using their public API. It includes topics like phishing, malware, hacking, threat intelligence, forensics, SIEM, OSINT, and more — ideal for cybersecurity researchers, analysts, and students.

> 🔁 **Updated every 3 days** via GitHub Actions.

---

## 📦 Live Dataset JSON

👉 [Click here to view the latest datasets (JSON)](https://raw.githubusercontent.com/rokibulroni/zenodo-datasets-index/main/data/zenodo_datasets.json)

---

## 🧠 What's Inside?

Each dataset entry includes:

* ✅ Dataset title
* ✅ Short description
* ✅ DOI and publication date
* ✅ Authors/creators
* ✅ Direct link to the dataset on Zenodo
* ✅ Topics/tags (if available)

---

## ⚙️ How It Works

This repo uses:

* 🐍 A Python script (`scripts/update_zenodo_datasets.py`) that fetches and formats raw Zenodo API data
* 🤖 A GitHub Actions workflow (`.github/workflows/update_zenodo.yml`) that:

  * Runs every 3 days automatically
  * Converts raw API results into clean JSON
  * Commits the output to `data/zenodo_datasets.json`

---

## 📜 API Used

We use this Zenodo API with carefully curated keywords:

```
https://zenodo.org/api/records?q=cybersecurity+phishing+malware+ransomware+hacking+forensic+pentest+ids+ips+siem+zeroday+exploit+ddos+threat+mitre+nmap+network+firewall+vulnerability+reverse+osint+incident+log+password+encryption+soc+mitigation+cybercrime+cti+breach+suricata+yara+wireshark+anomaly+dfir+cyberattack&type=dataset&size=300
```

---

## ✅ Use Case

You can integrate the generated JSON file into any web app, dashboard, or dataset browser. No backend required — just fetch and display using JavaScript, React, Vue, or any frontend framework.

---

## 👨‍💻 Author

Created and maintained by [**Rokibul Islam Roni**](https://rokibulroni.com)
🔗 [https://rokibulroni.com](https://rokibulroni.com)

---

## 📖 License

This repo only curates publicly available dataset metadata and is intended for educational and research use only.
 

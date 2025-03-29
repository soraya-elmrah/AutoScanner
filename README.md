# AutoScanner - Dashboard de sécurité pour images Docker 📦🔐

## 🎯 Objectif
AutoScanner est un outil interactif de supervision des vulnérabilités détectées par Trivy sur des images Docker. Il permet aux équipes sécurité et DevOps de visualiser, filtrer, exporter et tracer les résultats des scans de manière simple et efficace.

## 📸 Aperçu rapide
- 📥 Upload de plusieurs rapports `.json` générés par Trivy
- 📊 KPIs dynamiques (vulnérabilités, critiques, images scannées)
- 📈 Graphique des vulnérabilités par sévérité
- 📋 Tableau filtrable
- 💾 Export CSV des vulnérabilités filtrées
- 🕒 Horodatage automatique de chaque scan

## ⚙️ Technologies utilisées
- Python 3.10+
- Streamlit
- Pandas
- Trivy (scanner open source de vulnérabilités)

## 🧰 Installation locale

### 1. Cloner le projet
```bash
git clone <url_du_repo>
cd autoscan
```

### 2. Créer un environnement virtuel
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Installer Trivy
```bash
sudo apt install wget apt-transport-https gnupg lsb-release -y
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo gpg --dearmor -o /usr/share/keyrings/trivy.gpg
echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/trivy.list
sudo apt update && sudo apt install trivy -y
```

### 5. Scanner une image Docker avec Trivy
```bash
docker pull python:3.10-slim
mkdir -p data/reports
trivy image --format json -o data/reports/python310.json python:3.10-slim
```

### 6. Lancer le dashboard
```bash
PYTHONPATH=. streamlit run app/dashboard.py
```

📍 Accède ensuite à : http://localhost:8501

## ✅ Fonctionnalités disponibles
- Upload multi-fichiers JSON
- Analyse automatisée avec horodatage
- Visualisation par KPI et graphique
- Filtres interactifs par sévérité
- Export CSV des vulnérabilités filtrées

## 📁 Structure du projet
```
autoscan/
├── app/
│   └── dashboard.py         # Interface Streamlit
├── autoscan/
│   ├── parser.py            # Parsing JSON Trivy
│   ├── scanner.py           # (optionnel) Lancer Trivy automatiquement
│   └── utils.py             # Fonctions diverses (filtres, export...)
├── data/
│   └── reports/             # Fichiers JSON scannés
├── main.py
├── requirements.txt
└── README.md
```

---

## 🙋‍♀️ Auteur
Soraya El Mrah – Étudiante en cybersécurité, Télécom SudParis / IP Paris

## 🔐 Licence
MIT

---
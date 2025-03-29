import json
import pandas as pd

def load_trivy_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    all_records = []

    results = data.get("Results", [])  # <- important : Trivy stocke ça dans "Results"
    for result in results:
        target = result.get("Target", "Unknown Image")
        vulnerabilities = result.get("Vulnerabilities", [])

        for vuln in vulnerabilities:
            record = {
                "Image": target,
                "CVE": vuln.get("VulnerabilityID"),
                "Package": vuln.get("PkgName"),
                "Version": vuln.get("InstalledVersion"),
                "Severity": vuln.get("Severity"),
                "Description": vuln.get("Description"),
            }
            all_records.append(record)

    df = pd.DataFrame(all_records)
    return df
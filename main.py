from src.parser import load_trivy_json

if __name__ == "__main__":
    df = load_trivy_json("data/reports/python310.json")
    print(df.head())  # Aperçu des premières lignes

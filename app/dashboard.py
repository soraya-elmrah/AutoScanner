import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import tempfile
from autoscan.parser import load_trivy_json

def main():
    st.set_page_config(page_title="Docker Vulnerability Dashboard", layout="wide")

    st.title("🔍 Docker Vulnerability Dashboard")
    st.markdown("Analyse multi-fichiers des vulnérabilités détectées par Trivy.")

    uploaded_files = st.file_uploader("📤 Charger un ou plusieurs fichiers JSON de Trivy", type=["json"], accept_multiple_files=True)

    if uploaded_files:
        all_dfs = []

        for uploaded_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_path = tmp.name

            try:
                df = load_trivy_json(tmp_path)
                all_dfs.append(df)
            except Exception as e:
                st.error(f"Erreur lors du chargement de {uploaded_file.name} : {e}")

        if all_dfs:
            full_df = pd.concat(all_dfs, ignore_index=True)

            st.subheader("📈 KPIs Sécurité")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total vulnérabilités", len(full_df))
            col2.metric("Vulnérabilités critiques", (full_df["Severity"] == "CRITICAL").sum())
            col3.metric("Images analysées", full_df["Image"].nunique())

            st.subheader("📊 Répartition par sévérité")
            severity_counts = full_df["Severity"].value_counts().sort_index()
            st.bar_chart(severity_counts)

            st.subheader("📋 Liste complète (filtrable)")
            selected_severity = st.multiselect(
                "Filtrer par sévérité :", options=full_df["Severity"].unique().tolist(), default=full_df["Severity"].unique()
            )
            filtered_df = full_df[full_df["Severity"].isin(selected_severity)]
            st.dataframe(filtered_df)

            st.subheader("💾 Export")
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Télécharger les résultats filtrés (CSV)",
                data=csv,
                file_name="vulnerabilites_filtrees.csv",
                mime="text/csv",
            )

            scan_dates = filtered_df["ScanDate"].unique()
            st.info(f"🕒 Scans réalisés à : {', '.join(scan_dates)}")

    else:
        st.warning("Veuillez charger un ou plusieurs fichiers JSON pour commencer l’analyse.")

if __name__ == "__main__":
    main()

"""
Pour éviter de faire planter le notebookk à cause de la taille du dataframe , je vais créer une fonction
qui génère le scatter-plot et l'exporte au format png et html sans l'afficher dans le notebook.

"""


import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
import plotly.io as pio
pio.templates.default = "plotly_dark"
import pandas as pd
import plotly.express as px
import os


def plot_rfm_segment(df_or_path, output_dir="output", filename_base="scatter_rfm"):
    
    
    # Charger le DataFrame si on donne un chemin
    if isinstance(df_or_path, str):
        df = pd.read_csv(df_or_path)
    else:
        df = df_or_path.copy()
        
        
    color_map = {
    'Premium': '#FFD700',     
    'Fidèles': '#2ECC71',     
    'Inactifs': '#808080',    
    'À Réactiver': '#FF0000',
    'Nouveaux': '#0000FF'     
}
    
    # Vérification des colonnes requises
    required_cols = ['Recency', 'Frequency', 'Monetary', 'segment']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Colonne requise manquante : {col}")
    
    # Créer le dossier de sortie si besoin
    os.makedirs(output_dir, exist_ok=True)
    
    # Création du graphique interactif avec Plotly
    fig = px.scatter(
        df,
        x='Recency',  
        y='Monetary',  
        size='Frequency', 
        color='segment',  
        color_discrete_map=color_map,
        hover_data={
            'Recency': True,
            'Frequency': True,
            'Monetary': True,
            'segment': True
        },
        title="Scatter plot 2D: Récence vs Montant (taille = Frequency)",
        template="plotly_dark",
        size_max=30,
        opacity=0.7
    )

    # Personnalisation 
    fig.update_layout(
        title_font_size=22,
        xaxis_title="Recency (jours depuis le dernier achat)",
        yaxis_title="Montant total dépensé (Monetary)",
        legend_title="Segment :",
        font=dict(color="white"),
        plot_bgcolor='black',
        paper_bgcolor='black'
    )

    # Fichiers de sortie
    html_path = os.path.join(output_dir, f"{filename_base}.html")
    png_path = os.path.join(output_dir, f"{filename_base}.png")
    
    # Sauvegarde HTML (graphique interactif)
    fig.write_html(html_path)

    # Sauvegarde PNG (graphique statique) - nécessite kaleido
    try:
        fig.write_image(png_path, format="png", scale=2)
    except Exception as e:
        print(f"[⚠️] Erreur lors de la sauvegarde PNG : {e}")
    
    return {"html": html_path, "png": png_path}


############################TEST#####################################

rfm = pd.read_csv ("rfm_final_export.csv")

if __name__ == '__main__':
    plot_rfm_segment(rfm)



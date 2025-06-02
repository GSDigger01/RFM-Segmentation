# RFM Segmentation

Ce projet vise à mettre en place une segmentation client basée sur les métriques RFM : Récence, Fréquence et Montant.  
L’analyse a été réalisée sur un jeu de données de ventes contenant plus de 6 millions de lignes.

L’objectif principal est d’identifier des groupes de clients distincts pour améliorer le ciblage marketing, optimiser les campagnes et proposer des actions adaptées à chaque profil.

## Contenu du projet

- `RFM_clean.ipynb` : notebook principal contenant les étapes de traitement, de scoring et de visualisation.
- `clean_notebook.py` : fonction utilitaire pour nettoyer un notebook (variables et sorties).
- `Scatter_plot_fx.py` : fonction pour créer un scatter plot 2D avec plotly 
- `Output/` : dossier contenant les visualisations statiques au format PNG et le scatter plot interractif (html).

## Visualisations

Les graphiques ont été réalisés avec la librairie Plotly (graphiques interactifs).  
Note : ces visualisations ne s’affichent pas directement sur GitHub, car elles sont au format HTML.  
Vous pouvez les visualiser en téléchargeant le notebook ou via ce lien:  https://gsdigger01.github.io/RFM-Segmentation/. 

## À noter

- Les segments RFM sont définis selon des règles simples et orientées métier.
- Plusieurs versions statiques des graphiques sont disponibles pour faciliter la lecture.


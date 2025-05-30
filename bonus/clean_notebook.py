import nbformat
from nbformat.v4.nbbase import new_notebook
import os

def clean_notebook(input_path, output_path=None):
    """
    Nettoie un notebook Jupyter en supprimant tous les outputs
    et en réinitialisant les compteurs d'exécution.

    Parameters:
    - input_path : str : chemin vers le notebook original
    - output_path : str : chemin vers le notebook nettoyé (optionnel)
    """

    # Charger le notebook original
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Supprimer les outputs et compteurs d'exécution
    for cell in nb.cells:
        if cell.cell_type == 'code':
            cell['outputs'] = []
            cell['execution_count'] = None
            # Supprime les erreurs éventuelles
            if 'execution_count' in cell:
                cell['execution_count'] = None
            if 'metadata' in cell:
                cell['metadata'] = {}

    # Définir le chemin de sortie si non fourni
    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = base + '_clean' + ext

    # Enregistrer le notebook nettoyé
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    print(f"Notebook nettoyé enregistré sous : {output_path}")

# Exemple d'utilisation

if __name__ == '__main__':
    clean_notebook('Scatter_plot-2D.ipynb')

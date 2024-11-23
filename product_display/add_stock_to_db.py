import pandas as pd
import random

# Charger le fichier CSV
file_path = "product_display/products/amazon.csv"  # Remplacez par le chemin vers votre fichier
data = pd.read_csv(file_path)



# Ajouter une colonne de stock avec des valeurs aléatoires entre 0 et 500
data['stock'] = [max(random.normalvariate(100, 10),0) for _ in range(len(data))]

# Sauvegarder le fichier avec la colonne stock ajoutée
output_file_path = "fichier_avec_stock.csv"
data.to_csv(output_file_path, index=False)

print(f"Le fichier avec les stocks a été enregistré sous : {output_file_path}")

import pandas as pd
import random

# Charger le fichier CSV
file_path = "product_display/products/amazon.csv"  # Remplacez par le chemin vers votre fichier
data = pd.read_csv(file_path)



# Ajouter une colonne de stock avec des valeurs aléatoires entre 0 et 500
data['stock'] = [int(max(random.normalvariate(100, 10),0)) for _ in range(len(data))]

# Sauvegarder le fichier avec la colonne stock ajoutée
data.to_csv(file_path, index=False)

print(f"Le fichier avec les stocks a été enregistré sous : {file_path}")



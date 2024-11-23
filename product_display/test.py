import pandas as pd

# Charger les données CSV
file_path = 'products/amazon.csv'
data = pd.read_csv(file_path)

# Filtrer les colonnes nécessaires pour le modèle
data = data.rename(columns={
    "product_name": "name",
    "discounted_price": "discounted_price",
    "actual_price": "actual_price",
    "about_product": "description",
    "img_link": "image_url",
    "product_link": "product_url"
})

# Ajouter un champ de modèle supplémentaire pour Django
data['model'] = 'products.product'
data['pk'] = range(1, len(data) + 1)  # Ajouter des IDs uniques

# Créer une structure compatible avec Django
fixtures = []
for _, row in data.iterrows():
    fixtures.append({
        "model": row['model'],
        "pk": row['pk'],
        "fields": {
            "name": row['name'],
            "discounted_price": row['discounted_price'],
            "actual_price": row['actual_price'],
            "description": row['description'],
            "image_url": row['image_url'],
            "product_url": row['product_url']
        }
    })

# Sauvegarder dans un fichier JSON
output_path = 'products/fixtures/products.json'
with open(output_path, 'w', encoding='utf-8') as f:
    import json
    json.dump(fixtures, f, ensure_ascii=False, indent=4)

print(f"Fixture saved to {output_path}")

import json

# Charger le fichier JSON
with open('train_annotations.json') as f:
    data = json.load(f)

# Convertir les clés de la catégorie "images" en nombres
data['images'] = {int(k): v for k, v in data['images'].items()}

# Maintenant, les clés dans 'images' sont des nombres, et vous pouvez les manipuler comme tel

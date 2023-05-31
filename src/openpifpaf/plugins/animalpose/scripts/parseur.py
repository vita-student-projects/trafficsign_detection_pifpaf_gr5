import json

# Charger le fichier JSON
with open('val_annotations.json') as f:
    data = json.load(f)

# Parcourir les annotations et leur ajouter un 'id'
for i, annotation in enumerate(data['annotations'], 1):
    new_annotation = {'id': i}
    new_annotation.update(annotation)
    data['annotations'][i-1] = new_annotation

# Sauvegarder le fichier JSON modifié
with open('fichier_modifie.json', 'w') as f:
    json.dump(data, f, indent=4)

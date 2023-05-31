import csv
import json

def csv_to_json(csv_file, json_file):
    data = {"images": {}}
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            image_id = row["IMAGE_ID"]
            image_name = row["IMAGE_NAME"]
            data["images"][image_id] = image_name
    
    with open(json_file, 'w') as file:
        json.dump(data, file)

# Appel de la fonction avec le nom de votre fichier CSV d'entrée et le nom du fichier JSON de sortie
csv_to_json('test_annotations.csv', 'test_annotations.json')
import csv
import json

csv_file_1 = 'test_annotations.csv'
csv_file_2 = 'corner.csv'
json_file = 'test_test_annot.json'

annotations = []

# Parse du premier fichier CSV
with open(csv_file_1, 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=',')

    for row in csv_reader:
        image_id = int(row['IMAGE_ID'])
        bboxes = eval(row['BBOX'])
        categories = eval(row['CATEGORY'])

        if not bboxes:  
            bbox = [0, 0, 0, 0]
            category = 0
            annotation = {
                'image_id': image_id,
                'bbox': bbox,
                'keypoints': [[0, 0, 0] for _ in range(4)],
                'num_keypoints': 4,
                'category_id': category
            }
            annotations.append(annotation)
        else:
            if len(bboxes) == len(categories):
                for bbox, category in zip(bboxes, categories):
                    annotation = {
                        'image_id': image_id,
                        'bbox': bbox,
                        'keypoints': [[0, 0, 0] for _ in range(4)],
                        'num_keypoints': 4,
                        'category_id': category
                    }
                    annotations.append(annotation)
            else:
                print(f"Le nombre de bboxes et de catégories ne correspond pas pour l'image {image_id}")

# Initialisation d'un dictionnaire pour suivre la dernière annotation mise à jour pour chaque image
last_updated_annotation = {}

# Parse du deuxième fichier CSV
with open(csv_file_2, 'r') as file:
    csv_reader = csv.reader(file)

    next(csv_reader)  # Ignore the header row

    for row in csv_reader:
        image_id = int(row[0])
        keypoints = [eval(point) for point in row[1:]]

        start_index = last_updated_annotation.get(image_id, 0)
        for index in range(start_index, len(annotations)):
            if annotations[index]['image_id'] == image_id:
                num_keypoints = min(4, len(keypoints))
                annotations[index]['keypoints'][:num_keypoints] = keypoints[:num_keypoints]
                annotations[index]['num_keypoints'] = num_keypoints
                last_updated_annotation[image_id] = index + 1
                break
        else:
            print(f"Aucune annotation trouvée pour l'image {image_id} après l'index {start_index}")

# Génération du fichier JSON
result = {'annotations': annotations}

with open(json_file, 'w') as output_file:
    json.dump(result, output_file, indent=4)

print(f"Le fichier JSON a été enregistré sous le nom '{json_file}'.")


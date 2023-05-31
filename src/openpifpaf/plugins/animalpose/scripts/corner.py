import csv

def get_corners(bbox):
    if bbox is None:
        return []
    x, y, width, height = bbox
    return [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]

def extract_bbox_corners(csv_file):
    bbox_corners = []
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            image_id = row["IMAGE_ID"]
            bbox_str = row["BBOX"].strip('[]')
            if bbox_str:
                try:
                    bbox = list(map(float, bbox_str.split(',')))
                    corners = get_corners(bbox)
                    if len(corners) == 4:
                        bbox_corners.append((image_id, *corners))
                except ValueError:
                    print(f"Error converting BBOX to floats: {bbox_str}")
    
    return bbox_corners

def write_bbox_corners_to_csv(bbox_corners, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["IMAGE_ID", "X1", "Y1", "X2", "Y2", "X3", "Y3", "X4", "Y4"])
        writer.writerows(bbox_corners)

# Appel de la fonction avec le nom de votre fichier CSV en tant qu'argument
bbox_corners = extract_bbox_corners('test_annotations.csv')

# Écriture des valeurs de coins des BBOX dans un nouveau fichier CSV
write_bbox_corners_to_csv(bbox_corners, 'corner.csv')

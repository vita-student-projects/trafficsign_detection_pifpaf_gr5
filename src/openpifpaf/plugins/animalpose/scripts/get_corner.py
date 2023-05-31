
import csv
from datasets import load_dataset
from PIL import Image


ds = load_dataset("keremberke/german-traffic-sign-detection", name="full")
example = ds['train'][1]['image']
print(ds['train'][1]['objects']['category'])

#example.show()



def get_corners(bbox):
    if bbox is None:
        return []
    x, y, width, height = bbox
    return [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]

def get_boxes_data(dataset):
    """ input: dataset type = 'train', 'test', 'val'
    output: the 4 corners coordinates of the points in the order
    bot left --> bot right --> top right --> top left 
    """
    
    bbox_values = []
    for obj in ds[dataset]['objects']:
        if 'bbox' in obj:
            if isinstance(obj['bbox'], list):
                bbox_values.extend(obj['bbox'])
            else:
                bbox_values.append(obj['bbox'])

    corners_list = [get_corners(bbox) for bbox in bbox_values]
    
    return corners_list


corners = get_boxes_data('test')
i = 0
with open('test_annotations.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['IMAGE_ID','IMAGE_NAME','BBOX', 'CATEGORY','X1', 'Y1', 'X2', 'Y2', 'X3', 'Y3', 'X4', 'Y4'])

        
    for corner in corners:
        image_id = ds['test'][i]['image_id']
        image_name = ds['test'][i]['image']
        bbox = ds['test'][i]['objects']['bbox']
        x1, y1 = corner[0]
        x2, y2 = corner[1]
        x3, y3 = corner[2]
        x4, y4 = corner[3]
        cat = ds['test'][i]['objects']['category']
        writer.writerow([image_id, image_name, bbox, cat, x1, y1, x2, y2, x3, y3, x4, y4])
        i = i+1



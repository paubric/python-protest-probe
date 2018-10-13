import Algorithmia
import numpy as np
import matplotlib.pyplot as plt
import cv2

image_number = 13

input = {
  "image": "data://paubric3/protest_data/" + str(image_number) + ".jpg",
  "output": "data://paubric3/protest_data/" + str(image_number) + "_result.jpg",
  "min_score": 0.1,
  "max_boxes": 10000,
  "model": "faster_rcnn_inception_resnet_v2_atrous"
}

client = Algorithmia.client('simUTMULmOWj/OpAO9AUMXk+sFX1')
algo = client.algo('deeplearning/ObjectDetectionCOCO/0.2.1')

result = algo.pipe(input).result
count = len(result['boxes'])

print(result)
print('Count: ', count)

dir = client.dir("data://paubric3/protest_data/")
file = dir.file(str(image_number) + "_result.jpg").getBytes()
file = np.asarray(bytearray(file), dtype=np.uint8)
img = cv2.imdecode(file, 1)

plt.imshow(img)
plt.show()

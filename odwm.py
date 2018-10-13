import Algorithmia

image_number = 9

input = {
  "imageUrl": "data://paubric3/protest_data/" + str(image_number) + ".jpg",
  "modelUrl": "data://opencv/SampleModels/haarcascade_fullbody.xml",
  "outputUrl": "data://paubric3/protest_data/" + str(image_number) + "_result.jpg"
}
client = Algorithmia.client('simUTMULmOWj/OpAO9AUMXk+sFX1')
algo = client.algo('opencv/ObjectDetectionWithModels/0.1.51')
print(algo.pipe(input).result)

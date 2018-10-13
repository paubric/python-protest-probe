import Algorithmia

image_number = 1

input = {
  "image": "data://paubric3/protest_data/" + str(image_number) + ".jpg",
  "output": "data://paubric3/protest_data/" + str(image_number) + "_result.jpg",
  "min_score": 0.1
}
client = Algorithmia.client('simUTMULmOWj/OpAO9AUMXk+sFX1')
algo = client.algo('zeryx/openimagesDemo/0.2.0')
print(algo.pipe(input).result)

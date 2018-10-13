import Algorithmia

image_number = 1

input = {
    "image":[
      "data://paubric3/protest_data/1.jpg",
      "data://paubric3/protest_data/2.jpg",
      "data://paubric3/protest_data/3.jpg",
      "data://paubric3/protest_data/4.jpg",
      "data://paubric3/protest_data/5.jpg",
      "data://paubric3/protest_data/6.jpg",
      "data://paubric3/protest_data/7.jpg",
      "data://paubric3/protest_data/8.jpg",
      "data://paubric3/protest_data/9.jpg",
      "data://paubric3/protest_data/10.jpg",
      "data://paubric3/protest_data/12.jpg",
      "data://paubric3/protest_data/13.jpg",
      "data://paubric3/protest_data/14.jpg",
      "data://paubric3/protest_data/15.jpg",
      "data://paubric3/protest_data/16.jpg",
      "data://paubric3/protest_data/17.jpg",
      "data://paubric3/protest_data/18.jpg",
   ]

}
client = Algorithmia.client('simUTMULmOWj/OpAO9AUMXk+sFX1')
algo = client.algo('deeplearning/CrowdCounter/0.3.0')
print(algo.pipe(input).result)

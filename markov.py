import random

class Markov:

    def generate_text(trainingData_location : str, nGram_order : int, output_size : int):


        trainingData = open(trainingData_location,'r').read()

        traininglength = len(trainingData)

        generated_hashMap = {}

        for i in range(traininglength - nGram_order - 1):
    
            gram = trainingData[i: i + nGram_order]

            if gram not in trainingData.keys():
                trainingData[gram] = []

            generated_hashMap[gram].append(trainingData[ i + nGram_order ])
        

        currentGram = trainingData[ 0 : nGram_order ]

        result = currentGram

        for i in range(output_size):

            try:
                possibilities = generated_hashMap[currentGram]
            except:
                continue

            next = random.choice(possibilities)

            result += next

            currentGram = result[ len(result) - nGram_order : len(result)  ]

        
        return result



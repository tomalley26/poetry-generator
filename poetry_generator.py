import spacy
from spacy import displacy
from textblob import TextBlob
nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("/Users/tomalley/poetry-generator/.venv/lib/python3.11/site-packages/en_core_web_md")
import random
from nltk.corpus import wordnet
#import syllables

from createNGram import CreateNGram
from findSimilar import FindSimilar
from evaluation import Evaluation
from geneticAlg import GeneticAlgorithm
#from syllableCounter import SyllableCounter

class PoetryGenerator():
    def __init__(self):

        self.test = 0
        
        #self.run(initial_poem_list)

    def ask_theme(self):
        theme = input("What is your poetry theme? Choose one of 'love', 'nature', 'culture': ")
        return theme


    def choose_poem_in_theme(self):
        #theme = input("What is your poetry theme? Choose one of 'love', 'nature', 'culture': ")
        theme = self.ask_theme()

        if theme == "love":
            love_poems = [""]
            randomInt = random.randint(1, len(love_poems) - 1)
            poem_title = love_poems[randomInt]

        if theme == "nature":
            nature_poems = ["Volcanoes.txt", "Danez Smith.txt", "Pat Mora.txt" \
                , "Linda Park.txt"]
            randomInt = random.randint(1, len(nature_poems) - 1)
            poem_title = nature_poems[randomInt]

        if theme == "culture":
            culture_poems = ["Nikki Giovanni.txt", "Teresa Pham-Carsillo.txt", \
                "Bay Leaves.txt"]
            randomInt = random.randint(1, len(culture_poems) - 1)
            poem_title = culture_poems[randomInt]

        print("THIS IS POEM TITLE", poem_title)

        return poem_title


    def run(self, poem_title):
        # needs to return a dictionary of poem to novelty score

        inspiring_set = {}

        i = 0

        while i < 5:

            obj = CreateNGram([])

            filename = poem_title

            obj.populateNGramArray(filename)

            j = 0
            newPoem = ""

            while j < 5:
                randomInt = random.randint(1, 40)
                newPoem += obj.nGrams[randomInt] + "\n"
                j+=1
            #print("here is new poem")
            #print(newPoem)

            nGramPoem = newPoem

            # testing out some new stuf
            doc = nlp(newPoem)

            obj2 = FindSimilar("")

            for token in doc:
                #print(token, token.tag_)
                if token.tag_ == "NN":
                    print("HERE IS NOUN", token)
                    newPoem = newPoem.replace(str(token), obj2.findSynonyms(str(token)))

            #obj3 = SyllableCounter()
            #obj3.countSyllables(newPoem)

            print("Here is new poem one of 5", newPoem)

            obj3 = Evaluation()
            novelty_score = obj3.get_novelty_score(newPoem, nGramPoem)

            inspiring_set.update({newPoem: novelty_score})

            i += 1

        #self.print_to_results(newPoem)

        print("Here is inspiring set", inspiring_set)


        return inspiring_set

    def print_to_results(self, poem):
        with open ('/Users/tomalley/poetry-generator/Results.txt', 'a') as f:
            f.write('\n')
            f.write(poem)
        f.close()

    def call_genetic_alg(self):

        inspiring_set = self.run(self.choose_poem_in_theme())

        obj3 = GeneticAlgorithm()

        finalPoem = obj3.evolve(inspiring_set)

        #print(finalPoem)
        return finalPoem


def main():

    main_obj = PoetryGenerator()
    main_obj.call_genetic_alg()

    #poem = PoetryGenerator()
    #return poem

if __name__ == '__main__':
    main()

    
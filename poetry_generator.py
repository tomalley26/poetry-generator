import spacy
from spacy import displacy
from textblob import TextBlob
nlp = spacy.load("en_core_web_sm")
import random
from nltk.corpus import wordnet

from createNGram import CreateNGram
from findSimilar import FindSimilar
from evaluation import Evaluation
from geneticAlg import GeneticAlgorithm

class PoetryGenerator():
    """Generates short poems based on a theme using an inspiring set, n-grams,
    a synonym generator, and a genetic algorithm. Evaluates poems based on
    novelty and user feedback.
    """
    def __init__(self):

        self.test = 0

    def ask_theme(self):
        """ Asks user for theme of poem to generate.
        """
        theme = input("What is your poetry theme? Choose one of 'love', 'nature', 'culture': ")
        return theme

    def choose_poem_in_theme(self):
        """ Based on user's theme choice, randomly pick a poem from the inspiring set.
        """
        theme = self.ask_theme()

        if theme == "love":
            love_poems = ["Pablo Nerudo.txt", "Emily Bronte.txt", "Joy Harjo.txt", \
                "Lord Byron.txt"]
            randomInt = random.randint(0, len(love_poems) - 1)
            poem_title = love_poems[randomInt]

        if theme == "nature":
            nature_poems = ["Emily Dickinson.txt", "Danez Smith.txt", "Pat Mora.txt" \
                , "Linda Park.txt", "Mary Oliver.txt"]
            randomInt = random.randint(0, len(nature_poems) - 1)
            poem_title = nature_poems[randomInt]

        if theme == "culture":
            culture_poems = ["Nikki Giovanni.txt", "Teresa Pham-Carsillo.txt", \
                "Nikki Giovanni2.txt", "Suzanne Rancourt.txt", \
                    "Sally Wen Mao.txt"]
            randomInt = random.randint(0, len(culture_poems) - 1)
            poem_title = culture_poems[randomInt]

        return poem_title


    def run(self, poem_title):
        """ Calls CreateNGram class to create n-grams out of inspiring poem,
        randomly chooses five n-grams to create new poem, replaces nouns with
        generated synonyms, and gets novelty score. Repeats this process to
        create an inspiring set of n-gram poems and their scores, stored in
        a dictionary. Returns this dictionary for the genetic algorithm to use.
        """

        inspiring_set = {}

        i = 0

        # Adding five poems and their scores to the inspiring set dict

        while i < 5:

            obj = CreateNGram([])

            filename = poem_title

            obj.populateNGramArray(filename)

            j = 0
            newPoem = ""

            # Randomly picking five n-grams to create new poem

            while j < 5:
                randomInt = random.randint(1, len(obj.nGrams) - 1)
                newPoem += obj.nGrams[randomInt] + "\n"
                j+=1

            nGramPoem = newPoem

            doc = nlp(newPoem)

            # Finding nouns in poem, getting synonyms / antonyms of those nouns,
            # and replacing original nouns with a randomly chosen synonym / antonym

            obj2 = FindSimilar("")

            for token in doc:
                if token.tag_ == "NN":
                    newPoem = newPoem.replace(str(token), obj2.findSynonyms(str(token)))

            # Getting novelty score of poem

            obj3 = Evaluation()
            novelty_score = obj3.get_novelty_score(newPoem, nGramPoem)

            # Adding poem and score to inspiring set dict

            inspiring_set.update({newPoem: novelty_score})

            i += 1

        return inspiring_set

    def print_to_results(self, poem, score):
        """ Prints final poem and score to Results.txt file
        """
        with open ('/Users/tomalley/poetry-generator/Results.txt', 'a') as f:
            f.write('\n')
            f.write(poem)
            f.write('\n')
            f.write("Score: " + str(score))
            f.write('\n')
        f.close()

    def call_genetic_alg(self):
        """ Calls run method to get inspiring set dictionary,
        then calls genetic algorithm to create final poem, then
        gets evaluative score and returns both poem and score
        """

        inspiring_set = self.run(self.choose_poem_in_theme())

        obj3 = GeneticAlgorithm()

        # Runs the genetic algorithm on the inspiring set dictionary (5 poems and scores
        # made of n-grams from the orignal inspiring poem)

        finalPoem, score = obj3.evolve(inspiring_set)

        # Computing overall evaluation score

        obj4 = Evaluation()

        user_score_like, user_score_theme = obj4.get_user_score()
        final_score = obj4.compute_final_score(score, user_score_like, user_score_theme)

        print("Here's final score ", final_score)

        self.print_to_results(finalPoem, final_score)
        return finalPoem, final_score


def main():

    main_obj = PoetryGenerator()
    main_obj.call_genetic_alg()

if __name__ == '__main__':
    main()
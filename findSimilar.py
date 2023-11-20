from nltk.corpus import wordnet
import random
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")

class FindSimilar():
    def __init__(self, similarWords):
        
        self.similarWords = similarWords

    def findSynonyms(self, sourceWord):
        synonyms = []
        antonyms = []

        for syn in wordnet.synsets(sourceWord):
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
    
        synonyms = set(synonyms)
        antonyms = set(antonyms)

        print("Here is synonyms", synonyms)

        print("Here is antonyms", antonyms)

        # if random int = 1, use antonym of word. If 2, synonym
        syn_or_ant = random.randint(0,5)
        print("here's syn or ant", syn_or_ant)

        if syn_or_ant == 0:
            # use antonym
            if len(antonyms) == 0:
                return sourceWord 
            else:
                randomInt = random.randint(0, len(antonyms) - 1)

                print("chosen antonym: ", str(list(antonyms)[randomInt]))

                return str(list(antonyms)[randomInt])

        elif syn_or_ant != 0:
            # use synonym
            if len(synonyms) == 0:
                return sourceWord 
            else:
                randomInt = random.randint(0, len(synonyms) - 1)

                print("chosen synonym: ", str(list(synonyms)[randomInt]))

                return str(list(synonyms)[randomInt])

        """

        word1 = nlp(sourceWord)
        word2 = nlp(list(synonyms)[randomInt])

        print(word2)

        print(word1.similarity(word2))

        return str(word2)

        """
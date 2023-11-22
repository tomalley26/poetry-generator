from nltk.corpus import wordnet
import random
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")

class FindSimilar():
    """ Given a noun, finds synonyms and antonyms
    """
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

        # if random int = 1, use antonym of word. If random int = 2, use synonym of word.
        syn_or_ant = random.randint(0,5)

        if syn_or_ant == 0:
            # use antonym
            if len(antonyms) == 0:
                return sourceWord 
            else:
                randomInt = random.randint(0, len(antonyms) - 1)

                return str(list(antonyms)[randomInt])

        elif syn_or_ant != 0:
            # use synonym
            if len(synonyms) == 0:
                return sourceWord 
            else:
                randomInt = random.randint(0, len(synonyms) - 1)

                return str(list(synonyms)[randomInt])
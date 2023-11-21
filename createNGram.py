from textblob import TextBlob

class CreateNGram():
    """ Creates an array of n-grams given an inspiring poem
    """
    def __init__(self, nGrams):
        
        self.test = 0
        self.nGrams = nGrams

    def populateNGramArray(self, filename):
        """ Uses TextBlob's n-gram creation tool to take in a file with a poem
        and returns an array of that poem's n-grams.
        """

        with open("/Users/tomalley/poetry-generator/poems/" + filename) as f:

            poem = TextBlob(f.read())

        for ngram in poem.ngrams(n=4):
            string = ""
            for word in ngram:
                string += word + " "
            self.nGrams.append(string)
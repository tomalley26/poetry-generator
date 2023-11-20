from textblob import TextBlob

class CreateNGram():
    def __init__(self, nGrams):
        
        self.test = 0
        self.nGrams = nGrams

    def populateNGramArray(self, filename):

        with open("/Users/tomalley/poetry-generator/poems/" + filename) as f:

            poem = TextBlob(f.read())

        for ngram in poem.ngrams(n=4):
            string = ""
            for word in ngram:
                string += word + " "
            self.nGrams.append(string)

        #print("here is nGrams")
        #print(self.nGrams)
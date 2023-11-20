class Evaluation():
    def __init__(self) -> None:
        pass

    def get_novelty_score(self, oldPoem, newPoem):
        oldPoemSet = set()
        newPoemSet = set()

        for word in oldPoem.split():
            #print("word", word)
            oldPoemSet.add(word)

        for word in newPoem.split():
            newPoemSet.add(word)


        
        print("set", oldPoemSet)
        print("set", newPoemSet)

        diff = oldPoemSet.difference(newPoemSet)
        print("here is diff", diff)

        print("here is len of diff", len(diff))

        # divide len of diff by n(of n grams) * lines in poem

        return len(diff)
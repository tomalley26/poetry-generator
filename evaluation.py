class Evaluation():
    """ Produces and returns novelty score and user scores for final poem
    """
    def __init__(self) -> None:
        pass

    def get_novelty_score(self, oldPoem, newPoem):
        """ Finds how many words were replaced between old poem and new poem,
        assigns that value to novelty score
        """
        oldPoemSet = set()
        newPoemSet = set()

        for word in oldPoem.split():
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

    def get_user_score(self):
        """Asks user for 'soft' scores: likability and relation to original theme"""

        user_score_like = input("On a scale of 0-5, how much do you like this poem? ")

        user_score_theme = input("On a scale of 0-5, how much does the poem align with its theme? ")

        return user_score_like, user_score_theme

    def compute_final_score(self, novelty_score, user_score_like, user_score_theme):
        """Combines novelty and user scores into a final score"""
        return int(novelty_score) + int(user_score_like) + int(user_score_theme)

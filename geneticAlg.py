import random

class GeneticAlgorithm():
    """ Calls genetic algorithm for five crossovers and returns final poem
    """
    def __init__(self) -> None:
        pass

    def evolve(self, inspiringSet):
        """ Performs the five crossovers
        """

        poemOne = list(inspiringSet.keys())[0]
        score = inspiringSet.get(poemOne)

        i = 1

        while i < len(inspiringSet):
            poemOne, score = self.genetic_algorithm(poemOne, score, \
                list(inspiringSet.keys())[i], inspiringSet.get(list(inspiringSet.keys())[i]))
            i += 1

        print("HERE IS FINAL POEM \n", poemOne)
        return poemOne, score

    def genetic_algorithm(self, poemOne, score1, poemTwo, score2):
        """ Takes in two poems and their scores, splits them on a pivot point,
        chooses which section has the higher score and appends the higher scoring
        sections together to make a new poem. The new poem's novelty score will be
        the highest score out of the two argument poems. Standardizes poems to
        a length of five lines.
        """

        # find random pivot point
        randomInt = random.randint(0, 4)

        i = 0

        poemOneTop = ""

        poemOneBottom = ""

        poemTwoTop = ""

        poemTwoBottom = ""

        # split both poems on that pivot point

        while i < randomInt:
            poemOneTop += poemOne.split('\n')[i]
            poemOneTop += '\n'

            poemTwoTop += poemTwo.split('\n')[i]
            poemTwoTop += '\n'
            i += 1

        while i < 5:
            poemOneBottom += poemOne.split('\n')[i]
            poemOneBottom += '\n'

            poemTwoBottom += poemTwo.split('\n')[i]
            poemTwoBottom += '\n'
            i += 1

        # evaluate novelty score for each new section
                # (randomInt / 5) * poem's novelty score

        score1Top = (randomInt / 5) * score1
        score1Bottom = ((5-randomInt) / 5) * score1

        score2Top = (randomInt / 5) * score1
        score2Bottom = ((5-randomInt) / 5) * score1

        newPoem = ""

        # Poem 1: If top section scores higher than bottom section, 
        # append top section to new poem. Else, vice versa.

        if score1Top >= score1Bottom:
            newPoem += poemOneTop
            newPoem += '\n'
        else:
            newPoem += poemOneBottom
            newPoem += '\n'

        # Poem 2: If top section scores higher than bottom section, 
        # append top section to new poem. Else, vice versa.

        if score2Top >= score2Bottom:
            newPoem += poemTwoTop
        else:
            newPoem += poemTwoBottom

        # Deleting any empty whitespaces between lines:

        actualNewPoem = ""

        for line in newPoem.split('\n'):
            if len(line) != 0:
                actualNewPoem += line
                actualNewPoem += '\n'

        # Standardizing poem to five lines

        shortenedPoem = ""

        j = 0

        num_of_lines = 0

        for line in actualNewPoem.split('\n'):
            num_of_lines += 1

        if num_of_lines > 5:

            while j < 5:
                shortenedPoem += actualNewPoem.split('\n')[j]
                shortenedPoem += '\n'
                j += 1

        # Return new poem and its corresponding novelty score

        return shortenedPoem, max(score1, score2)
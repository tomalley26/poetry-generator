import random

class GeneticAlgorithm():
    def __init__(self) -> None:
        pass

    def evolve(self, inspiringSet):

        print("in evolve")

        print("here is poemOne", list(inspiringSet.keys())[0])


        poemOne = list(inspiringSet.keys())[0]
        score = inspiringSet.get(poemOne)
        print(inspiringSet.get(poemOne))

        i = 1

        #poemOne = self.genetic_algorithm(poemOne, inspiringSet.get(poemOne), \
            #list(inspiringSet.keys())[i], inspiringSet.get(list(inspiringSet.keys())[i]))

        while i < len(inspiringSet):
            poemOne, score = self.genetic_algorithm(poemOne, score, \
                list(inspiringSet.keys())[i], inspiringSet.get(list(inspiringSet.keys())[i]))
            i += 1

        print("HERE IS FINAL POEM \n", poemOne)
        return poemOne, score

    def genetic_algorithm(self, poemOne, score1, poemTwo, score2):

        print("here is poem 2\n")
        print(poemTwo)

        #print("in GA here is 1", poemOne)
        #print("in GA here is 2", poemTwo)

        # find random pivot point
        randomInt = random.randint(0, 4)
        # split both poems on that pivot point

        i = 0

        #print("split 1", poemTwo.split('\n')[1])

        poemOneTop = ""

        poemOneBottom = ""

        poemTwoTop = ""

        poemTwoBottom = ""

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

        print("here is top and bottoms")

        print("1 top \n")

        print(poemOneTop)

        print("1 bottom \n")
        print(poemOneBottom)

        print("2 top \n")

        print(poemTwoTop)

        print("2 bottom \n")
        print(poemTwoBottom)

        # evaluate novelty score for each new section
                # just do (randomInt / 5) * poem's novelty score

        score1Top = (randomInt / 5) * score1
        score1Bottom = ((5-randomInt) / 5) * score1

        score2Top = (randomInt / 5) * score1
        score2Bottom = ((5-randomInt) / 5) * score1

        # choose section from poemOne with largest novelty

        # choose section from poemTwo with largest novelty score

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

        # return newPoem and its corresponding novelty score

        print("HERE IS NEW POEM", newPoem)

        actualNewPoem = ""

        for line in newPoem.split('\n'):
            print("LINE", line)
            if len(line) != 0:
                actualNewPoem += line
                actualNewPoem += '\n'

        shortenedPoem = ""

        j = 0
        while j < 5:
            shortenedPoem += actualNewPoem.split('\n')[j]
            shortenedPoem += '\n'
            j += 1

        #print("HERE IS SHORTENED POEM", shortenedPoem)

        return shortenedPoem, max(score1, score2)
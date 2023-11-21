# poetry-generator

## Themed Short Poem Generator

### Set up

How to set up and run the code.

1. If not using the included .venv, create your own virtual environment and download spacy, TextBlob, random, nltk.corpus, and flask.

2. Make sure that any hardcoded paths in the code are replaced with your own local paths. For example, search "/Users/tomalley/poetry-generator/" and replace that with the new path.

3. Running locally: cd into the project directory (make sure you're in the correct virtual environment) and run your version of ```python3 (insert local path here)/poetry-generator/poetry-generator.py```

Respond to the prompts for theme, likability score, and theme score.

You will see the poem printed in the terminal.

4. Running website: cd into the project directory (make sure you're in the correct virtual environment) and run ```flask --app hello run```

Follow the url where the website is being temporarily hosted (e.g. http://127.0.0.1:5000)

Refresh the webpage (so that it will be suspended in loading mode), then come back to the terminal

Respond to the prompts for theme and scores.

Return to the webpage, where you will see the outputted poem and corresponding score.

Click the "Hear this poem!" button to hear it read aloud.


### Work Description

This poetry generation system takes in an inspiring set of poems in the theme categories of love, nature, and culture. Once the user inputs a theme, a poem from that theme is randomly chosen as the inspiring poem. After the poem is chosen, I used TextBlob's ngrams tool to make n-grams (currently 4-grams) out of the poem, and add all of those n-grams to an array. Then I randomly choose a few n-grams from that array (currently 5) to add to a new poem (each n-gram being one line of the poem). This new poem forms the base upon which some words will be replaced and a simple genetic algorithm will be run. 

I then extract the nouns from the poem using spacy's token tags, and then use nltk.corpus with Wordnet to find synonyms and antonyms for those words. I then randomly choose a synonym or antonym to replace that noun with, and if a word is replaced, I add points to the poem's novelty score. The novelty score is loosely based on the distance from the original n-gram poem to the final outputted poem. 

The genetic algorithm repeats the above process of creating poems out of n-grams five times. Each poem, and its corresponding novelty score, is added to a dictionary. The genetic algorithm then takes the first poem in that dictionary, and 'evolves' it by comparison to the remaining poems in the dictionary. For each 'generation' (pair of poems), the algorithm chooses a random pivot point to split each poem on. It then calculates the novelty score of the top and bottom parts of each poem, and chooses the portion of each poem with the highest novelty score. These two portions are appending to each other to create a new poem that will go on to be part of the next generation.

In order to keep the length of the poems consistent, the produced poems are then shortened to (currently 5) lines. For future work, I would explore different ways to standardize poem length without devaluing the role that the lines below each pivot point have in the genetic algorithm.

Lastly, the final poem is printed to the terminal and the user is prompted for evaluation. The user will evaluate a poem based on how much they like the poem, and how relevant it is to the theme they originally chose. These scores are combined with the poem's existing novelty score to produce a final evaluative score.

You can also view previously created poems and their scores in the Results.txt file.


### Challenges

At the onset of this project, I was initially challenged to think of ways that I could combine concepts learned in class to the totally novel endeavor of creating a poetry generating system. I experimented with tools such as spacy and TextBlob, and looked into how they turn words into tokens that can be classified into parts of speech and more. I wasn't initially sure how I would use these tools for poetry generation, since I needed a method of ensuring accurate semantics even if I had access to a sentence's part of speech. After discovering the power that n-grams have in preserving some meaning and semantics of a sentence while simultaneously serving as building blocks for a poem, I decided that I wanted to base my poems on n-grams. Another challenge was figuring out how to work in an inspiring set. I decided to search the web on my own for poems in particular themes that I was personally inspired or impressed by. I organized the favorite poems I found into three themes meaningful to me: love, nature, and culture. Creating n-grams of these poems I enjoyed served as a solid base for further creative changes. I was also challenged in thinking about multiple creative ways of changing poems once I had this base. I spent time learning how to use tools in nltk to find synonyms, and designed a genetic algorithm to make sure that any poems I produced were vastly different from the poems I was inspired by. Overall, I was most challenged and rewarded by the process of choosing which tools to use, maintaining the theme and semantics of a poem, and pursuing the goal of novel creation.

### Scholarly Inspiration

'Constrained creation of poetic forms during theme-driven exploration of a domain defined by an N-gram model'

https://www.tandfonline.com/doi/full/10.1080/09540091.2015.1130024

#### Notes:

I was inspired by these authors' emphasis on content theme and free-form poetry, rather than having a fixed form. They also left room for their system to produce a variety of aesthetics (some better than others), and to produce a variety of results that may be surprising.


'Language chunking, data sparseness, and the value of a long marker list: explorations with word n-grams and authorial attribution'

https://academic.oup.com/dsh/article/29/2/147/975278

#### Notes:

This article inspired me to consider the optimal length of n-grams use to generate my poetry. After experimentation, I felt that 1-grams were not helpful in retaining the semantics of my inspiring poems, and that 3-grams could still make the semantics of generated poems confusing. I ended up settling on 4-grams, since they provided a good balance of understandable semantics and creative opportunities.

'Research on Community Competition and Adaptive Genetic Algorithm for Automatic Generation of Tang Poetry'

https://www.hindawi.com/journals/mpe/2016/4076154/

#### Notes:

This article inspired me to consider the use of genetic algorithms in my system. It also allowed me to reflect on the connections between preserving tradition and cultural background of a poem while revolutionizing the process of creating a poem. This system's main focus was to produce Tang Dynasty-style poetry. I appreciated this strong cultural foundation for the system, and used these ideas to inspire my own themes and chosen poems.

### Additional Resources:

https://getcssscan.com/css-buttons-examples

https://thinkinfi.com/how-to-download-nltk-corpus-manually/

https://www.guru99.com/wordnet-nltk.html

https://www.holisticseo.digital/python-seo/nltk/wordnet


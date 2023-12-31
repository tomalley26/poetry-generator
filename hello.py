from flask import Flask
from flask import render_template
from poetry_generator import PoetryGenerator

app = Flask(__name__)

@app.route("/")

def hello_world():
    """ Using python and flask to call my poetry generator, get the final poem and score,
    and display it on a webpage.
    """
    
    poem, score = PoetryGenerator().call_genetic_alg()
    ttsString = ""
    line1 = poem.split('\n')[0]
    line2 = poem.split('\n')[1]
    line3 = poem.split('\n')[2]
    line4 = poem.split('\n')[3]
    line5 = poem.split('\n')[4]

    for line in poem:
        ttsString += line.strip('\n')
    print(ttsString)

    return render_template(
        'index.html',
        my_poem=ttsString,
        poem_score=score,
        line_1 = line1,
        line_2 = line2,
        line_3 = line3,
        line_4 = line4,
        line_5 = line5
    )
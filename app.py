from flask import Flask, render_template
from game_of_life import *


app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(25, 25)
    return render_template('index.html')


@app.route('/live')
def live():
    gameoflife = GameOfLife()
    if gameoflife.counter > 0:
        gameoflife.form_new_generation()
    gameoflife.counter += 1
    return render_template('live.html', gameoflife=gameoflife)


if __name__ == '__main__':
    app.run(debug=True)

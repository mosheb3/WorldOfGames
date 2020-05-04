## Moshe Barazani
## Date: 03-05-2020
## filename: webServer.py

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    fr = open("data/data.json", "r")
    posts_json_a = fr.readlines()
    fr.close()

    #print(posts_json_a)

    posts_json_b = "["+(json.dumps(posts_json_a)[2:-2])+"]"

    user = {'username': 'WorldOfGames'}

    #posts_json = [{'gamername': 'moshe1', 'game_name': 'guess', 'score': 123123},
    #              {'gamername': 'moshe2', 'game_name': 'guess', 'score': 12341234},
    #              {'gamername': 'moshe3', 'game_name': 'guess', 'score': 1234512345}]
    return render_template('score.html', title='WorldOfGames', user=user, posts=eval(posts_json_b))

app.run('127.0.0.1', '8081', debug=True)
## Moshe Barazani
## Date: 03-05-2020
## filename: webServer.py
from Utils import *
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/clean', methods=['GET', 'POST'])

def index():
    fr = open("data/data.json", "r")
    posts_json_a = fr.readlines()
    fr.close()

    posts_json_b = "["+(json.dumps(posts_json_a)[2:-2])+"]"
    user = {'username': 'WorldOfGames'}

    return render_template('score.html', title='WorldOfGames', user=user, posts=eval(posts_json_b))

def clean():
    fw = open("data/data.json", "w+")
    fw.writelines("")
    fw.close()
    return render_template('clean.html')

if __name__ == "__main__":
    app.run('127.0.0.1', '8081', debug=True)

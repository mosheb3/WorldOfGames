## Moshe Barazani
## Date: 03-05-2020
## filename: webServer.py

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():
    fr = open("data/data.json", "r")
    posts_json_a = fr.readlines()
    fr.close()

    posts_json_b = "["+(json.dumps(posts_json_a)[2:-2])+"]"
    user = {'username': 'WorldOfGames'}

    return render_template('score.html', title='WorldOfGames', user=user, posts=eval(posts_json_b))

if __name__ == "__main__":
    app.run('0.0.0.0', '8081', debug=True)
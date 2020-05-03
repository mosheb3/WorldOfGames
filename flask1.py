from flask import Flask, render_template

app1 = Flask(__name__)

@app1.route('/', methods=['GET', 'POST'])
def index_page_landing():
    return render_template('index.html')
if __name__ == "__main__":
    #app1.run('127.0.0.1:8081')
    app1.run('127.0.0.1','8081')

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/myteam")
def myteam():
    return render_template('nav/myteam.html')

@app.route("/playershop")
def playershop():
    return render_template('nav/playershop.html')

@app.route("/playerstats")
def playerstats():
    return render_template('nav/playerstats.html')

@app.route("/leaderboards")
def section2():
    return render_template('nav/leaderboards.html')

@app.route("/gameschedule")
def gameschedule():
    return render_template('nav/gameschedule.html')


if __name__ == '__main__':
    app.run(debug=True)
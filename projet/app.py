from random import randint 

from flask import Flask, jsonify, render_template, Response, request, redirect, url_for
import pymongo
from pymongo import MongoClient

app = Flask(__name__,static_url_path='/static')
score=0
streak=0


def get_db():
    client = MongoClient('mongodb://mongodb:27017/')
    db = client["score"]

    return db

def get_score():
    db = get_db()
    _scores = db.score_tb.find().sort("score",pymongo.DESCENDING).limit(10)
    scores = [{"name": s["name"], "score": s["score"]} for s in _scores]
    return scores

def roulette():
    x=randint(1,6)
    return (x!=6)


@app.route("/roll/", methods=['POST'])
def roll():
    global score
    global streak
    rolled=roulette()
    if rolled:
        streak+=1
        score+=10*streak
        return render_template('roll.html', scorehtml=score, streakhtml=streak)
    streak=0
    score=0
    return render_template('fail.html')

@app.route("/save/", methods=['POST'])
def save():
    player_name = request.form.get("player_name")
    print(player_name)
    print(request.form.get("player_name"))
    if not player_name:
        player_name="anonymous"
    global score
    global streak
    db=get_db()
    dbscore=db["score_tb"]
    score_save={"score":score,"name":player_name}
    dbscore.insert_one(score_save)
    return redirect(url_for('index'))
    


@app.route('/')
def index():
    global scores
    global streak
    score=0
    streak=0
    scores=get_score()
    return render_template('index.html', scorehtml=score, streakhtml=streak, lenhtml=len(scores), scoresboard=scores)

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

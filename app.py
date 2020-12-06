from flask import (Flask, request, jsonify)
from flask import g, jsonify, Response
from flask import render_template
import sqlite3
import json
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

DATABASE = 'acler.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def select_random_utterance(cursor):
    cursor.execute("SELECT rowid, phrase, intent FROM active_learning WHERE is_ok IS NULL AND type='check' ORDER BY RANDOM() LIMIT 1;")
    result = cursor.fetchone()
    if result:
        return dict(result)
    else:
        return {}

def select_random_utterance_tag(cursor):
    cursor.execute("SELECT rowid, phrase, intent FROM active_learning WHERE final_tag IS NULL AND type='tag' ORDER BY RANDOM() LIMIT 1;")
    result = cursor.fetchone()
    if result:
        res_dict = dict(result)
        res_dict["intent"] = json.loads(res_dict["intent"])
        return res_dict
    else:
        return {}

@app.route('/')
def index():
    return render_template('home.html')


@app.route("/active_learning/",methods=["GET"])
def active_learning_main():
    return render_template("active_learning.html")

@app.route("/active_learning/tag",methods=["GET"])
def active_learning_tag():
    return render_template("active_learning_tag.html")

@app.route("/active_learning/check",methods=["GET"])
def active_learning_check():
    return render_template("active_learning_check.html")


@app.route("/active_learning/check/random",methods=["GET"])
def get_random_utterance():
    cur = get_db().cursor()
    sample = select_random_utterance(cur)
    print(sample)
    if len(sample)>0:
        return render_template('active_learning_check_single.html',sample=sample)
    else:
        return render_template('all_done.html')

@app.route("/active_learning/check/update",methods=["POST"])
def active_learning_check_update():
    print(request.form)
    prep_stmt = "UPDATE active_learning SET is_ok=? WHERE rowid=?"
    conn = get_db()
    cur = conn.cursor()
    cur.execute(prep_stmt,[request.form["check"], request.form["phrase_id"]])
    conn.commit()
    return Response("",200)

@app.route("/active_learning/tag/random")
def get_random_utterance_for_tagging():
    cur = get_db().cursor()
    sample = select_random_utterance_tag(cur)
    if len(sample) > 0:
        return render_template('active_learning_tag_single.html', sample=sample)
    else:
        return render_template('all_done.html')

@app.route("/active_learning/tag/update",methods=["POST"])
def active_learning_tag_update():
    print(request.form)
    prep_stmt = "UPDATE active_learning SET final_tag=? WHERE rowid=?"
    conn = get_db()
    cur = conn.cursor()
    cur.execute(prep_stmt,[request.form["check"], request.form["phrase_id"]])
    conn.commit()
    return Response("",200)

if __name__ == "__main__":
    app.run(debug=True)

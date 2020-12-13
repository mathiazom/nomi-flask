import os
from flask import Flask, render_template, request, redirect, session
import csv
from random import choice

app = Flask(__name__)

app.secret_key = "xyz"

def read_csv_rows(filename):
    f = open(filename)
    reader = csv.reader(f,delimiter=",")
    rows = [row for row in reader]
    f.close()
    return rows

def words_from_rows(rows):
    return [r[0] for r in rows]

def read_words_from_csv(filename):
    return words_from_rows(read_csv_rows(filename))

@app.route('/')
def main():
    adjective = session.pop('adjective',None)
    noun = session.pop('noun',None)
    if not adjective or not noun:
        adjectives = read_words_from_csv("adjectives.csv")
        adjective = choice(adjectives)
        nouns = read_words_from_csv("nouns.csv")
        noun = choice(nouns)
    return render_template('nomi.html',adjective=adjective,noun=noun)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

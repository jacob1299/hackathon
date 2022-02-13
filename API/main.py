from flask import Flask, request, render_template
from board import Board
from flask_cors import CORS

app = Flask("")
CORS(app)

@app.route("/hello")
def hello():
	return {"hello": "world"}

@app.route("/board")
def board():
	b = Board()
	b.make_default_board()
	return(str(b))

@app.route("/game")
def game():
	return render_template("main.html", color="black")

app.run(host='0.0.0.0')

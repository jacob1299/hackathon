from flask import Flask, request, render_template
from board import Board

app = Flask("")

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
	return render_template("main.html")

app.run(host='0.0.0.0')

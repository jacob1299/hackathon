from flask import Flask, request
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

app.run(host='0.0.0.0', port=8080)
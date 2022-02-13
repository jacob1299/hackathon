from flask import Flask, request, render_template
from board import Board
from game import Game
from flask_cors import CORS


app = Flask("")
CORS(app)

@app.route("/hello")
def hello():
	return {"hello": "world"}

@app.route("/game")
def game():
	return render_template("main.html", color="black")

@app.route("/games_status")
def gamestatus():
	result = dict()
	for game in Game.games.keys():
		result[game] = Game.getGameBoard(game).state + ", " + Game.getGameBoard(game).turn
	return result

@app.route('/make_game', methods = ['POST'])
def makegame():
	g = Game()
	return {"id" : g.name}

@app.route('/setup_state', methods = ['GET'])
def setup_state():
	data = dict(request.values)
	if len(data) != 2:
		return {"Success": "False"}
	id, player = data['id'], data['player']
	curr_board = Game.getGameBoard(id)
	result = "True" if curr_board.turn == player else "False"
	return {"ready":result}


@app.route('/set_pieces', methods = ['POST'])
def set_pieces():
	data = dict(request.values)
	if len(data) != 14:
		return {"Success" : "False", "len": len(data)}
	id, player = data['id'], data['player']

	curr_board = Game.getGameBoard(id)
	curr_board.set_pieces(data, player)
	curr_board.swap_turns()
	return curr_board.for_json()

app.run(host='0.0.0.0')

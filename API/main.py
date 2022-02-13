from flask import Flask, request, render_template
from board import Board
from game import Game

app = Flask("")

@app.route("/hello")
def hello():
	return {"hello": "world"}

@app.route("/game")
def game():
	return render_template("main.html")

@app.route("/games_status")
def gamestatus():
	result = dict()
	for game, board in Game.games.items():
		result[game] = "Running"
	return result

@app.route('/make_game', methods = ['GET'])
def makegame():
	g = Game()
	return {"id" : g.name}

@app.route('/setup_state', methods = ['GET'])
def setup_state():
	data = dict(request.values)
	if len(data) != 2:
		return {"Success", "False"}
	id, player = data['id'], data['player']
	curr_board = Game.getGameBoard(id)
	result = "True" if curr_board.turn == player else "False"
	return {"ready":result}


@app.route('/set_pieces', methods = ['GET'])
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

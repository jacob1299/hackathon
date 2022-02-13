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
	try:
		g = Game.games[request.args.get("id")]
		print(f"{g.players[0]}    {g.players[1]}")
		print(f"{request.args.get("user")}")
		return render_template("main.html", color="white", id=request.args.get("id"))
	except:


@app.route("/games_status")
def gamestatus():
	result = dict()
	for game in Game.games.keys():
		result[game] =  "Running, " + Game.getGameBoard(game).turn
	return result

@app.route('/make_game', methods = ['GET', 'POST'])
def makegame():
	g = Game(request.args.get("color"), request.args.get("ante"), request.args.get("user"))
	return {"link" : g.get_link()}

@app.route('/setup_state', methods = ['GET'])
def setup_state():
	data = dict(request.values)
	if len(data) != 2:
		return {"Success": "False"}
	id, player = data['id'], data['player']
	curr_board = Game.getGameBoard(id)
	result = "True" if curr_board.turn == player else "False"
	return {"ready":result}

@app.route('/board', methods=['GET'])
def getboard():
	data = dict(request.values)
	if len(data) != 1:
		return {"Success": "False"}
	id = data['id']
	curr_board = Game.getGameBoard(id)
	return curr_board.for_json()


@app.route('/move', methods=['POST'])
def make_move():
	data = dict(request.values)
	if len(data) != 3:
		return {"Success": "False"}

	id = data['id']
	origin, dest = data['from'], data['to']
	curr_board = Game.getGameBoard(id)

	success = curr_board.make_move(origin, dest)
	if (success):
		curr_board.swap_turns()
		return curr_board.for_json()
	else:
		return {"Success": "False, cannot move"}
		


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

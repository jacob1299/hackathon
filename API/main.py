from flask import Flask, request

app = Flask("")

@app.route("/hello")
def hello():
	return {"hello": "world"}

app.run(host='0.0.0.0', port=8080)
# ---- Flask Hello World ---- #

from flask import Flask

app = Flask(__name__)


@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	return "correctamente"

@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "Excelente"

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael" :
		return "Hola, {}".format(name)
	else :
		return "No encontrado", 404


if __name__ == "__main__":
	app.run()

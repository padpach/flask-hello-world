# ---- Flask Hello World ---- #

# Import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

#use los decoradores
#@app.route("/")
@app.route("/hello")

# define la vista usando una funcion que regresa una cadena

def hello_world():
	return "Hello, World"

# start the development server using the run() method
if __name__ == "__main__":
	app.run()

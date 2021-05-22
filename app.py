from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
	if request.method == "GET":
		#languages = ["C++", "Python", "PHP", "Java", "C", "Ruby",
		#			"R", "C#", "Dart", "Fortran", "Pascal", "Javascript", "how to train your dragon"]
		sentences = ["how to begin with java", "Javascript", "covid-19 resources",
					  "hunan province", "ultra music festival", "january jones",
					  "stephen colbert", "taco bell breakfast", "college board",
					  "zac efron", "johnny manziel", "miguel cabrera", "psych"]

		return render_template("index.html", sentences=sentences)


if __name__ == '__main__':
	app.run(debug=True)

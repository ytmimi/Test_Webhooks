from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
	return 'Hello World'


@app.route('/payload', methods=['POST'])
def payload():
	print(request.json)


if __name__ == '__main__':
	app.run(debug=True)
import json
from flask import Flask, request, make_response, render_template
from jinja2 import Template

app = Flask(__name__)

bulletin_board = []

@app.route("/")
def get_list():
    return render_template('list.html', items=bulletin_board)

@app.route("/item", methods=['PUT'])
def add_list():
    name = request.args.get('name')
    bulletin_board.append({'name': name})
    return make_response(json.dumps({'status': 'success'}))

if __name__ == "__main__":
    app.run(debug=True)

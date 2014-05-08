import string
import json
from flask import Flask, request, make_response

app = Flask(__name__)

bulletin_board = ['item 1', 'item 2']

@app.route("/")
def get_list():
    html = string.join([('<p>%s</p>' % item) for item in bulletin_board], '\n')
    return make_response(html)

@app.route("/item", methods=['PUT'])
def add_list():
    name = request.args.get('name')
    bulletin_board.append(name)
    return ''

if __name__ == "__main__":
    app.run(debug=True)

import string
import json
from flask import Flask, request, make_response

app = Flask(__name__)

todolist = []

@app.route("/")
def get_list():
    html = string.join([('<p>%s</p>' % item) for item in todolist], '\n')
    return make_response(html)

@app.route("/item", methods=['PUT'])
def add_list():
    name = request.args.get('name')
    todolist.append(name)
    return make_response(json.dumps({'status': 'success'}))

if __name__ == "__main__":
    app.run(debug=True)

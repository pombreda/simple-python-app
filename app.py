import string
import json
from flask import Flask, request, make_response
from jinja2 import Template

app = Flask(__name__)

todolist = []

list_template = Template("""
<h1>TODO List</h1>
{% if items %}
<ul>
  {% for item in items %}
  <li>{{ item }}</li>
  {% endfor %}
</ul>
{% else %}
[no items]
{% endif %}
""")

@app.route("/")
def get_list():
    out = list_template.render(items=todolist)
    return make_response(out)

@app.route("/item", methods=['PUT'])
def add_list():
    name = request.args.get('name')
    todolist.append(name)
    return make_response(json.dumps({'status': 'success'}))

if __name__ == "__main__":
    app.run(debug=True)

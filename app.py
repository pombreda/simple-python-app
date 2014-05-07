import string
import json
from datetime import datetime
from flask import Flask, request, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template

DB_CONFIG = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:////tmp/bbaas.db',
    'SQLALCHEMY_ECHO': False,
    'SECRET_KEY': '',
    'DEBUG': True,
}

app = Flask(__name__)
app.config.update(DB_CONFIG)
db = SQLAlchemy(app)

class BBItem(db.Model):
    def __init__(self, name):
        self.name = name
        self.time = datetime.utcnow()

    __tablename__ = 'board'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    pub_date = db.Column(db.DateTime)

@app.route("/")
def get_list():
    return render_template('list.html', items=BBItem.query.order_by(BBItem.pub_date.desc()).all())

@app.route("/item", methods=['PUT'])
def add_list():
    name = request.args.get('name')
    new_item = BBItem(name)
    db.session.add(new_item)
    db.session.commit()
    return make_response(json.dumps({'status': 'success'}))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

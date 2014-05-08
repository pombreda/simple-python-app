from flask import *

app = Flask(__name__)

# keep track of bulletin board state
bulletin_board = []

# route "/" -> returns the bulletin board HTML
@app.route('/')
def bb():
    # TODO
    return 'hello world'

# TODO route PUT "/item" -> adds item to bulletin board, returns some JSON indicating success

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""


def _quote_exists(existing_quote):
    """Recommended helper"""


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    pass


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    pass


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    pass


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    pass


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    pass
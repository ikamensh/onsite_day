import json

from flask import Flask, request
import os.path

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/team')
def get_team():
    team_id = request.args.get('team_id', 0)  # TODO: support getting the real data
    with open(os.path.join('example_json', 'team.json'), 'r') as f:
        return f.read()


@app.route('/user')
def get_user():
    user_id = request.args.get('user_id', 0)  # TODO: support getting the real data
    with open(os.path.join('example_json', 'user.json'), 'r') as f:
        return f.read().replace('"user_id": 1', f'"user_id": {user_id}')


@app.route('/results')
def get_results():
    # results maps day-> score, favorable users (with score better than 0)
    results = {
        0: dict(score=0, users=[]),
        1: dict(score=3, users=[1, 2, 3]),
        2: dict(score=3, users=[1, 2, 3]),
        3: dict(score=2, users=[1, 3]),
        4: dict(score=2, users=[1, 2]),
        5: dict(score=0, users=[]),
    }
    return json.dumps(results)


if __name__ == '__main__':
    app.run()

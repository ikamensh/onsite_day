import json

from flask import Flask, request
import os.path

import utils
from data_model.team import all_teams

app = Flask(__name__)


@app.route('/')
def hello_world():
    # TODO: return static content
    return 'Hello World!'


@app.route('/team')
def get_team():
    if 'team_id' not in request.args:
        return 'Team id is missing in the request.', 400

    team_id = request.args['team_id']  # TODO: support getting the real data
    with open(os.path.join('example_json', 'team.json'), 'r') as f:
        return f.read().replace('"team_id": 1', f'"team_id": {team_id}')


@app.route('/user')
def get_user():
    if 'user_id' not in request.args:
        return 'user_id is missing in the request.', 400
    user_id = request.args['user_id']  # TODO: support getting the real data
    with open(os.path.join('example_json', 'user.json'), 'r') as f:
        return f.read().replace('"user_id": 1', f'"user_id": {user_id}')


@app.route('/results')
def get_results():
    # TODO: error handling
    # results maps user-> scores, favorable users (with score better than 0)
    team_id = request.args['team_id']

    if team_id not in all_teams:
        return "invalid team id", 400
    return json.dumps(all_teams[team_id], default=utils.default_serialize)


@app.route('/rule', methods=['POST'])
def post_rule():
    pass


if __name__ == '__main__':
    app.run()

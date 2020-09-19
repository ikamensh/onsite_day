import json

from flask import Flask, request
import os.path

import utils
from persistence import get_team, get_user


app = Flask(__name__)


@app.route('/')
def hello_world():
    # TODO: return static content
    return 'Hello World!'


@app.route('/team')
def get_team():
    # results maps user-> scores, favorable users (with score better than 0)
    if 'team_id' not in request.args:
        return 'team_id is missing in the request.', 400
    team_id = request.args['team_id']

    try:
        team = get_team(team_id)
    except Exception as e:
        return f'invalid team id {e}', 400

    return json.dumps(team, default=utils.default_serialize)


@app.route('/user')
def user_route():
    if 'user_id' not in request.args:
        return 'user_id is missing in the request.', 400
    user_id = request.args['user_id']
    try:
        user = get_user(user_id)
    except Exception as e:
        return f'invalid user id {e}', 400

    return json.dumps(user, default=utils.default_serialize)


@app.route('/results')
def get_results():
    return "to be implemented"


@app.route('/rule', methods=['POST'])
def post_rule():
    if 'user_id' not in request.args:
        return 'user_id is missing in the request.', 400
    user_id = request.args['user_id']

    if 'day' not in request.args:
        return 'day is missing in the request.', 400
    day = request.args['day']

    if 'preference' not in request.args:
        return 'preference is missing in the request.', 400
    preference = request.args['preference']

    try:
        user = get_user(user_id)
    except Exception as e:
        return f'invalid user id {e}', 400

    if day == 0:
        user.monday = preference
    elif day == 1:
        user.tuesday = preference
    elif day == 2:
        user.wednesday = preference
    elif day == 3:
        user.thursday = preference
    elif day == 4:
        user.friday = preference
    else:
        return "invalid day id, must be between 0 and 4", 400

    return "successfully posted the rule", 200



if __name__ == '__main__':
    app.run()

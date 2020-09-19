import json
import os

from flask import Flask, request, send_from_directory

import utils
from persistence import get_team, get_user, load_data

load_data()  # Load in dummy data: TODO: change this once we have a real app
app = Flask(__name__, static_url_path='', static_folder='../frontend', template_folder='../frontend')


@app.route('/team')
def team_route():
    # results maps user-> scores, favorable users (with score better than 0)
    if 'team_id' not in request.args:
        return 'team_id is missing in the request.', 400
    team_id = int(request.args['team_id'])

    try:
        team = get_team(team_id)
    except Exception as e:
        return f'invalid team id {e}', 400

    return json.dumps(team, default=utils.default_serialize)


@app.route('/user')
def user_route():
    if 'user_id' not in request.args:
        return 'user_id is missing in the request.', 400
    user_id = int(request.args['user_id'])

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
    data = request.json
    if 'user_id' not in data:
        return 'user_id is missing in the request.', 400
    user_id = int(data['user_id'])

    if 'day' not in data:
        return 'day is missing in the request.', 400
    day = int(data['day'])

    if 'preference' not in data:
        return 'preference is missing in the request.', 400
    preference = int(data['preference'])

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

    return "Successfully posted the rule", 200


@app.route('/connect', methods=['POST'])
def connect():
    data = request.json

    # validate input
    if 'from' not in data:
        return 'from user_id is missing in the request.', 400
    user_from = int(data['from'])

    if 'to' not in data:
        return 'to user_id is missing in the request.', 400
    user_to = int(data['to'])

    if 'team_id' not in data:
        return 'team_id is missing in the request.', 400
    team_id = int(data['team_id'])

    # check no self loop
    if user_from == user_to:
        return "cannot want to work with yourself", 400

    # validate users
    try:
        get_user(user_from)
        get_user(user_to)
    except Exception as e:
        return f'invalid user id {e}', 400

    # validate team
    try:
        team = get_team(team_id)
    except Exception as e:
        return f'invalid team id {e}', 400

    team.add_connection(user_from, user_to)
    return "added connection", 200


@app.route('/')
def send_js():
    return send_from_directory(os.path.join(os.pardir, 'frontend'), 'index.html')


if __name__ == '__main__':
    app.run(debug=True)

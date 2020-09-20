from matplotlib import pyplot as plt
import seaborn as sns

import networkx as nx

from data_model.user import Weekdays
from persistence import load_data, get_team, get_user
import random

def plot_team_connections(team):
    G = nx.Graph()
    for user in team.users:
        G.add_node(user.first_name)

    for source, connections in team.connections.items():
        for target in connections:
            u1 = get_user(source)
            u2 = get_user(target)
            G.add_edge(u1.first_name, u2.first_name)

    import random
    pos = {n: (random.random(), random.random()) for n in G.nodes}

    nx.draw(
        G,
        pos=nx.fruchterman_reingold_layout(G, fixed=G.nodes, pos=pos, ),
        with_labels=True,
        node_size=3000,
    )
    plt.show()


def plot_liking(team):

    x = []
    y = []
    c = []

    for dy, user in enumerate(team.users):
        for i, day in enumerate(Weekdays.all_days):
            liking = getattr(user, day)
            x.append(i + dy * 0.07 - 0.07)
            y.append(liking)
            c.append(user.first_name)

    sns.scatterplot(x, y, c)
    # plt.scatter( x, y, c=c)
    plt.show()


if __name__ == '__main__':
    load_data()
    team = get_team(1)
    plot_team_connections(team)
    plot_liking(team)
import os

py_root = os.path.dirname(__file__)

data_folder = os.path.join(py_root, "data")
os.makedirs(data_folder, exist_ok=True)

teams_file = os.path.join(data_folder, "teams.json")

#!/bin/bash
set -euxo pipefail

pushd backend || exit
pip install -r requirements.txt
python _generate_example_jsons.py
python app.py

popd || exit
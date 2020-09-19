#!/bin/bash
set -euxo pipefail

pushd backend || exit
pip install -r requirements.txt
python app.py

popd || exit
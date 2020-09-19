#!/bin/bash
pushd backend || exit
pip install -r requirements.txt
python app.py
popd || exit
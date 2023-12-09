#!/bin/bash

mkdir -p docs/img
cp -r py/createDocs/docs/img docs/

python3 py/createDocs/runCreateDocs.py

bash mdtopdf.bash docs/en/SFGPL_docs docs/img docs/en
bash mdtopdf.bash docs/jp/SFGPL_docs docs/img docs/jp

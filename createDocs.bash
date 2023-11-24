#!/bin/bash
mkdir -p docs/img
cp -r py/createDocs/docs/img docs/

python3 py/createDocs/runCreateDocs.py

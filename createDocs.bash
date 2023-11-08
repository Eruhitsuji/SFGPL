#!/bin/bash
mkdir -p docs/img
cp -r py/createDocs/docs/img docs/
python3 py/createDocs/aboutSFGPL.py
python3 py/createDocs/sentence_pattern.py
python3 py/createDocs/Word.py
python3 py/createDocs/pronoun.py
python3 py/createDocs/negativeSentence.py
python3 py/createDocs/interrogativeSentence.py
python3 py/createDocs/imperativeSentence.py
python3 py/createDocs/verbConjugation.py
python3 py/createDocs/Modifier.py
python3 py/createDocs/partOfSpeechConversion.py
python3 py/createDocs/Conjunction.py
python3 py/createDocs/DeterminerN.py
python3 py/createDocs/version.py

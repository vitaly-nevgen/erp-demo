virtualenv env --python=/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
source env/bin/activate
pip install -U pip==22.1.2
pip install -r requirements.txt
deactivate
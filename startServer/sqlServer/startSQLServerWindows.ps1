# Make sure flask is installed
# pip install flask
$env:FLASK_APP = 'databaseServer.py'

flask run --host=localhost --port=5001

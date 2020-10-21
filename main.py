from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def mainPage():
    return 'Hello World'

givenUrl = ''

@app.before_request
def getUrl():
    print('request')
    print(request.args.getlist)

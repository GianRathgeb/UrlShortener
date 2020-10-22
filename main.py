from flask import Flask, request, redirect
app = Flask(__name__)


@app.route('/')
def mainPage():
    return 'Hello World'


givenUrl = ''

@app.route('/<path>')
def getUrl(path):
    return redirect(f"https://www.{path}", code=308)

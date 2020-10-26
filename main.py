from flask import Flask, request, redirect
app = Flask(__name__)


@app.route('/')
def mainPage():
    return 'Hello World'


@app.route('/<path>')
def getUrl(path):
    if path == "google":
        return redirect("https://www.google.ch", code=308)
    else:
        return redirect("/", code=308)

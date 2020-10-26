from flask import Flask, request, redirect

import url as urllist

app = Flask(__name__)


@app.route('/')
def mainPage():
    return 'Hello World'


@app.route('/<path>')
def getUrl(path):
    if path in urllist.url.keys():
        for short in urllist.url:
            if short == path:
                return redirect(urllist.url[short], code=308)
    else:
        return redirect("/", code=308)

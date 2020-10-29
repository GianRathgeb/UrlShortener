from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy

from databaseServer import db
db.create_all()
newUrl = AddNewUrl(urlShort='gea', urlLong='https://google.com')
db.session.add(newUrl)
db.session.commit()

AddNewUrl.query.all()

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

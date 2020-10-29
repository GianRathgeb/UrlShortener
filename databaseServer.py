from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_db_URI'] = 'localhost:5001/sql'

db = SQLAlchemy(app)

class AddNewUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    urlShort = db.Column(db.String(12), unique=True, nullable=False)
    urlLong = db.Column(db.String(255), unique=True, nullable=False)

    def __repr(self):
        return f'Long: {self.urlLong}'
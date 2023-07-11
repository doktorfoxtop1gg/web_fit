from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#app.config('SQLALCHEMY_DATABASE_URI') = 'sqlite:///shop.db'
#db = SQLAlchemy(app)

#сlass Item(db.Model):
#    id = db.Column(db.Integer, primaly_key=True)
#    title = db.Column(db.String(100), nullable=False)
#    price = db.Column(db.Integer, nullable=False)
#    isActive = db.Column(db.Boolean, default=True)
#    text = db.Column(db.Text, nullable=False)
#    def __repr__(self):
#        return '<Article %r>' % self.id

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/feedback')
def feedback():
    return render_template("feedback.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/register')
def register():
    return render_template("register.html")
    
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/sponsor')
def sponsor():
    return "Hello world"

@app.route('/delivery')
def delivery():
    return render_template("buy.html")


if __name__ == "__main__":
#    with app.app_context():
#        db.create_all()
    app.run(debug=True)
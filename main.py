from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
from datetime import datetime




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/codingthunder"

db = SQLAlchemy(app)




class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    link = db.Column(db.String(120), nullable=False)
    # img_file = db.Column(db.String(12), nullable=True)


@app.route("/", methods=['GET'])
def post_route():
    post = Posts.query.filter_by().all()
    return render_template('post.html', post=post)



app.run(debug=True)


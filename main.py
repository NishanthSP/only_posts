from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
from datetime import datetime




app = Flask(__name__)




@app.route("/")
def post_route():
    
    return render_template('post.html', post=post)



app.run(debug=True)


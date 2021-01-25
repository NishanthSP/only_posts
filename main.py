from flask import Flask, render_template, request


app = Flask(__name__)




@app.route("/")
def post_route():
    
    return render_template('post.html', post=post)



app.run(debug=True)


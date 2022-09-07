from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "Blev"
@app.route("/TT")
def index():
    
    return render_template("index.html")



def greet():
    return render_template("index.html")

from flask import Flask,render_template;

app = Flask(__name__)
app.config['STATIC_URL_PATH'] = '/static'
@app.route("/")
def hello_world():
    return render_template("home.html");

@app.route("/contact")
def contact():
    return render_template("contact.html");
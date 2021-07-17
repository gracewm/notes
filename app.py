from flask import Flask, render_template, request, session
from flask_session import Session
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config.update(SECRET_KEY=os.urandom(24))

app.config.from_object(__name__)
Session(app)

@app.route("/", methods=["GET", "POST"])
def index(): 
    if session.get("notes") is None:
        session["notes"]=[]
    if request.method == "POST":
        note = request.form.get("note")        
        session["notes"].append(note)
            
    return render_template("index.html", notes=session["notes"])
 
if __name__ == "__main__": 
    with app.test_request_context("/"):
        session["key"] = "value"
    app.run(host='0.0.0.0', port='5000') 


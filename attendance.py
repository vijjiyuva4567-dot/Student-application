# update
from flask import Flask, render_template, request

app = Flask(__name__)

attendance = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        status = request.form.get("status")
        if name and status in ["P", "A"]:
            attendance[name] = status

    return render_template("index.html", attendance=attendance)

if __name__ == "__main__":
    app.run(debug=True)

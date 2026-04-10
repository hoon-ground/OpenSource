from flask import Flask, render_template, request, redirect
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Log:
    id: int
    type: str
    title: str
    content: str

logs = []

@app.route("/")
def home():
    return render_template("home.html", logs=logs)

@app.route("/write", methods=["GET", "POST"])
def write():
    if request.method == "POST":
        log_type = request.form["type"]
        title = request.form["title"].strip()
        content = request.form["content"].strip()

        if not title or not content:
            return render_template("write.html")

        log_entry = Log(
            id=len(logs),
            type=log_type,
            title=title,
            content=content
        )

        logs.append(log_entry)
        return redirect("/")

    return render_template("write.html")

@app.route("/log/<int:id>")
def log_detail(id):
    log_entry = logs[id]
    return render_template("log.html", log=log_entry)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

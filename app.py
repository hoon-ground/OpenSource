from flask import Flask, render_template, request, redirect

app = Flask(__name__)

logs = []

@app.route("/")
def home():
    return render_template("home.html", logs=logs)


@app.route("/write", methods=["GET", "POST"])
def write():
    if request.method == "POST":
        log_type = request.form["type"]
        title = request.form["title"]
        content = request.form["content"]

        log = {
            "id": len(logs),
            "type": log_type,
            "title": title,
            "content": content
        }

        logs.append(log)
        return redirect("/")

    return render_template("write.html")


@app.route("/log/<int:id>")
def log_detail(id):
    log = logs[id]
    return render_template("log.html", log=log)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
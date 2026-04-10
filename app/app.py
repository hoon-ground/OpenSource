"""Dev.Log - A simple Flask-based logging application.

This module implements a web application for creating, storing, and viewing
development logs with different types (e.g., TIL, Bug Fix, Feature).
"""

from flask import Flask, render_template, request, redirect
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Log:
    """Represents a single log entry.

    Attributes:
        id (int): Unique identifier for the log entry.
        type (str): Category of the log (e.g., 'TIL', 'Bug Fix', 'Feature').
        title (str): Title or subject of the log entry.
        content (str): Main content/description of the log entry.
    """
    id: int
    type: str
    title: str
    content: str

logs = []

@app.route("/")
def home():
    """Display the home page with all log entries.

    Returns:
        str: Rendered HTML of the home page showing all logs.
    """
    return render_template("home.html", logs=logs)

@app.route("/write", methods=["GET", "POST"])
def write():
    """Handle log entry creation.

    GET: Display the log writing form.
    POST: Process form submission and create a new log entry.

    Returns:
        str: Rendered HTML of the write form or redirect to home page.
    """
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
    """Display detailed view of a specific log entry.

    Args:
        id (int): The ID of the log entry to display.

    Returns:
        str: Rendered HTML of the log detail page.
    """
    log_entry = logs[id]
    return render_template("log.html", log=log_entry)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

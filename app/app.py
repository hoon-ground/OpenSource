"""Dev.Log - A simple Flask-based logging application.

This module implements a web application for creating, storing, and viewing
development logs with different types (e.g., TIL, Bug Fix, Feature).
"""

from flask import Flask, render_template, request, redirect, jsonify
from flasgger import Flasgger
from dataclasses import dataclass, asdict
import os

# Set template and static folders relative to parent directory
app_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__,
            template_folder=os.path.join(app_dir, '..', 'templates'),
            static_folder=os.path.join(app_dir, '..', 'static'))
swagger = Flasgger(app)

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

@app.route("/api/logs", methods=["GET"])
def get_logs():
    """Get all log entries in JSON format.
    ---
    tags:
      - Logs
    summary: Retrieve all log entries
    description: Returns a list of all development log entries in JSON format.
    responses:
      200:
        description: Successfully retrieved all logs
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: Unique identifier of the log
              type:
                type: string
                description: Category of the log (TIL, Bug Fix, Feature, etc.)
              title:
                type: string
                description: Title of the log entry
              content:
                type: string
                description: Main content of the log entry
    """
    return jsonify([asdict(log) for log in logs])

@app.route("/api/logs", methods=["POST"])
def create_log_api():
    """Create a new log entry via API.
    ---
    tags:
      - Logs
    summary: Create a new log entry
    description: Creates a new log entry with the provided data.
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - type
            - title
            - content
          properties:
            type:
              type: string
              description: Category of the log
            title:
              type: string
              description: Title of the log entry
            content:
              type: string
              description: Main content of the log entry
    responses:
      201:
        description: Log entry successfully created
        schema:
          type: object
          properties:
            id:
              type: integer
            type:
              type: string
            title:
              type: string
            content:
              type: string
      400:
        description: Missing required fields
    """
    data = request.get_json()

    if not data or not data.get('title') or not data.get('content'):
        return jsonify({"error": "Missing required fields"}), 400

    new_log = Log(
        id=len(logs),
        type=data.get('type', 'General'),
        title=data.get('title'),
        content=data.get('content')
    )
    logs.append(new_log)
    return jsonify(asdict(new_log)), 201

@app.route("/api/logs/<int:id>", methods=["GET"])
def get_log_api(id):
    """Get a specific log entry by ID.
    ---
    tags:
      - Logs
    summary: Retrieve a specific log entry
    description: Returns a single log entry by its ID in JSON format.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the log entry to retrieve
    responses:
      200:
        description: Successfully retrieved the log
        schema:
          type: object
          properties:
            id:
              type: integer
            type:
              type: string
            title:
              type: string
            content:
              type: string
      404:
        description: Log entry not found
    """
    if id < 0 or id >= len(logs):
        return jsonify({"error": "Log not found"}), 404
    return jsonify(asdict(logs[id]))

@app.route("/api/logs/<int:id>", methods=["PUT"])
def update_log(id):
    """Update an existing log entry.
    ---
    tags:
      - Logs
    summary: Update a log entry
    description: Updates an existing log entry with provided data.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the log entry to update
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            type:
              type: string
              description: Category of the log
            title:
              type: string
              description: Title of the log entry
            content:
              type: string
              description: Main content of the log entry
    responses:
      200:
        description: Log entry successfully updated
        schema:
          type: object
          properties:
            id:
              type: integer
            type:
              type: string
            title:
              type: string
            content:
              type: string
      404:
        description: Log entry not found
    """
    if id < 0 or id >= len(logs):
        return jsonify({"error": "Log not found"}), 404

    data = request.get_json()
    log_entry = logs[id]

    if 'type' in data:
        log_entry.type = data['type']
    if 'title' in data:
        log_entry.title = data['title']
    if 'content' in data:
        log_entry.content = data['content']

    return jsonify(asdict(log_entry))

@app.route("/api/logs/<int:id>", methods=["DELETE"])
def delete_log(id):
    """Delete a log entry.
    ---
    tags:
      - Logs
    summary: Delete a log entry
    description: Deletes a log entry by its ID.
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID of the log entry to delete
    responses:
      200:
        description: Log entry successfully deleted
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: Log entry not found
    """
    if id < 0 or id >= len(logs):
        return jsonify({"error": "Log not found"}), 404

    deleted_log = logs.pop(id)
    # Reindex remaining logs
    for i, log in enumerate(logs):
        log.id = i

    return jsonify({"message": "Log deleted successfully"})

@app.route("/write", methods=["GET", "POST"])
def write():
    """Handle log entry creation.

    GET: Display the log writing form.
    POST: Process form submission and create a new log entry.

    Returns:
        str: Rendered HTML of the write form or redirect to home page.

    ---
    tags:
      - Web Pages
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

    ---
    tags:
      - Web Pages
    """
    log_entry = logs[id]
    return render_template("log.html", log=log_entry)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

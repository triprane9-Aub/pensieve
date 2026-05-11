"""Pensieve web UI — a magical interface for your memories."""

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

from pensieve import add_memory, load_memories

app = Flask(__name__)


@app.template_filter("pretty_date")
def pretty_date(iso_str):
    return datetime.fromisoformat(iso_str).strftime("%B %d, %Y · %I:%M %p")


@app.route("/")
def index():
    memories = list(reversed(load_memories()))
    return render_template("index.html", memories=memories)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text", "").strip()
    if text:
        add_memory(text)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5050)

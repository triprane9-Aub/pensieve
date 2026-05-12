"""Pensieve web UI — a magical interface for your memories."""

from datetime import datetime, date, timedelta
from itertools import groupby
from flask import Flask, render_template, request, redirect, url_for

from pensieve import add_memory, load_memories, delete_memory

app = Flask(__name__)


@app.template_filter("pretty_date")
def pretty_date(iso_str):
    return datetime.fromisoformat(iso_str).strftime("%B %d, %Y · %I:%M %p")


@app.template_filter("pretty_day")
def pretty_day(date_str):
    d = datetime.fromisoformat(date_str).date()
    today = datetime.now().date()
    if d == today:
        return f"Today  ·  {d.strftime('%B %d, %Y')}"
    if d == today - timedelta(days=1):
        return f"Yesterday  ·  {d.strftime('%B %d, %Y')}"
    return d.strftime('%B %d, %Y')


@app.route("/")
def index():
    memories = sorted(load_memories(), key=lambda m: m["timestamp"])
    groups = [
        {"date": date_str, "memories": list(day_mems)}
        for date_str, day_mems in groupby(memories, key=lambda m: m["timestamp"][:10])
    ]
    groups.reverse()
    return render_template("index.html", groups=groups)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text", "").strip()
    if text:
        add_memory(text)
    return redirect(url_for("index"))


@app.route("/delete/<int:memory_id>", methods=["POST"])
def delete(memory_id):
    delete_memory(memory_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=5050)

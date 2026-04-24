from flask import Flask, render_template, request, redirect
from datetime import date
from daycounter.counter import count_days, parse_date
import sqlite3
import logging

logging.basicConfig(filename="results.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def init_db():
    conn = sqlite3.connect("daycounter.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_date TEXT,
            end_date TEXT,
            days INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    history = []

    if request.method == "POST":
        start = request.form.get("start_date")
        end = request.form.get("end_date")

        try:
            start_date = parse_date(start)
            end_date = parse_date(end) if end else date.today()
            days = count_days(start_date, end_date)
            result = f"Number of days between {start} and {end or date.today()}: {days} days"

            # Log to file
            logging.info(result)

            # Save to SQLite
            conn = sqlite3.connect("daycounter.db")
            c = conn.cursor()
            c.execute("INSERT INTO results (start_date, end_date, days) VALUES (?, ?, ?)",
                      (start, str(end or date.today()), days))
            conn.commit()
            conn.close()

        except Exception as e:
            result = f"Error: {e}"

    # Fetch history
    conn = sqlite3.connect("daycounter.db")
    c = conn.cursor()
    c.execute("SELECT start_date, end_date, days, timestamp FROM results ORDER BY id DESC LIMIT 10")
    history = c.fetchall()
    conn.close()

    return render_template("index.html", result=result, history=history)


# ✅ NEW: Clear History Route
@app.route("/clear_history", methods=["POST"])
def clear_history():
    # Clear SQLite table
    conn = sqlite3.connect("daycounter.db")
    c = conn.cursor()
    c.execute("DELETE FROM results")
    conn.commit()
    conn.close()

    # Clear log file
    open("results.log", "w").close()

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



from flask import Flask, render_template, request
from datetime import date
from daycounter.counter import count_days, parse_date

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        start = request.form.get("start_date")
        end = request.form.get("end_date")

        try:
            start_date = parse_date(start)
            end_date = parse_date(end) if end else date.today()
            days = count_days(start_date, end_date)
            result = f"Number of days between {start} and {end or date.today()}: {days} days"
        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    # Run the app on all interfaces so you can access it from Windows browser too
    app.run(host="0.0.0.0", port=5000, debug=True)


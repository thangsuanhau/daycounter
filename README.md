Daycounter

Daycounter is a lightweight Python application that calculates the number of calendar days between two dates. It is useful for tracking elapsed time since a past event, measuring project timelines, or simply counting days between custom dates.

Features

Accepts a start date (e.g., the day of an event).

Uses either today’s date or a user‑defined end date.

Outputs the total number of days between the two points.

Can be run interactively (python app.py) or as a module (python -m daycounter).

Packaged with modern Python standards (pyproject.toml, setup.py) for easy installation.

Installation

Clone the repository and install in editable mode:

git clone https://github.com/thangsuanhau/daycounter.git
cd daycounter
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

Usage

Run interactively:

python src/daycounter/__main__.py

Or use the module shortcut:

python -m daycounter

Example:

📅 Calendar Day Counter
Enter start date (YYYY-MM-DD): 2024-01-01
Enter end date (YYYY-MM-DD) or press Enter for today:
Number of days between 2024-01-01 and 2026-04-24: 844

Testing

Run unit tests with:

pytest tests/

CI/CD

This project includes a GitHub Actions workflow (.github/workflows/ci.yml) to automatically run tests on each push.

License

Add your preferred license (MIT, Apache 2.0, etc.) in the LICENSE file.

Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Project Structure

daycounter/
├── .github/workflows/ci.yml
├── src/daycounter/
│   ├── __init__.py
│   ├── __main__.py
│   └── counter.py
├── tests/
│   └── test_counter.py
├── README.md
├── setup.py
├── pyproject.toml
└── LICENSE
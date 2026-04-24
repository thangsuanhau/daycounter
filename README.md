# Daycounter

Daycounter is a lightweight Python application that calculates the number of calendar days between two dates. It is useful for tracking elapsed time since a past event, measuring project timelines, or simply counting days between custom dates.

## Features
- Accepts a start date (e.g., the day of an event).
- Uses either today’s date or a user‑defined end date.
- Outputs the total number of days between the two points.
- Can be run interactively (`python app.py`) or as a module (`python -m daycounter`).
- Packaged with modern Python standards (`pyproject.toml`, `setup.py`) for easy installation.
- Includes a Flask web interface with input form and result display.
- Logs results to a file (`results.log`) for audit.
- Stores results in SQLite (`daycounter.db`) and shows recent history in the web interface.
- Provides a **Clear Result** button and a **Clear History** button (with confirmation) in the web interface.
---

## Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/thangsuanhau/daycounter.git
cd daycounter
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

Usage (CLI)
Run interactively:
python src/daycounter/__main__.py

Or use the module shortcut:
python -m daycounter

Example:
📅 Calendar Day Counter
Enter start date (YYYY-MM-DD): 2024-01-01
Enter end date (YYYY-MM-DD) or press Enter for today:
Number of days between 2024-01-01 and 2026-04-24: 844 days

Web Interface
You can also run Daycounter as a web app using Flask.

Setup
source .venv/bin/activate
pip install -r requirements.txt
python webapp.py

Run
Open your browser at:
http://localhost:5000/

Usage

Enter a start date (YYYY-MM-DD).
Optionally enter an end date (defaults to today if left blank).
Click Calculate to see the number of days.
Use the Clear Result button to reset the output.
Recent results are shown in a table on the right (from SQLite).
Use the Clear History button to wipe all stored results (with confirmation).

Testing
Run unit tests with:
pytest tests/

CI/CD
This project includes a GitHub Actions workflow (.github/workflows/ci.yml) to automatically run tests on each push.

Workflow Overview
Runs on every push and pull request.

Sets up Python 3.x.

Installs dependencies from requirements.txt.

Runs unit tests with pytest.

Example Workflow File:

name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: pytest

License
Add your preferred license (MIT, Apache 2.0, etc.) in the LICENSE file.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Project Structure

daycounter/
├── .github/workflows/ci.yml
├── .github/workflows/cd.yml
├── .github/workflows/python-tests.yml
├── src/daycounter/
│   ├── __init__.py
│   ├── __main__.py
│   └── counter.py
├── templates/
│   └── index.html
├── webapp.py
├── tests/
│   └── __init__.py
│   ├── test_counter.py
├── .gitignore
├── pyproject.toml
├── daycounter.db
├── README.md
├── requirements.txt
├── results.log
├── setup.py
└── LICENSE

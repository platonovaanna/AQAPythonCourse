# QA Automation Practice Project

This project contains automated API and UI tests written in Python using
Pytest, Requests and Playwright.

---

## 🚀 Technologies

- Python 3.10+
- Pytest
- Requests
- Playwright

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/platonovaanna/AQAPythonCourse.git
cd AQAPythonCourse
```

Create and activate virtual environment:

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

Add your ReqRes API key in `conftest.py`.

---

## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Run API tests:

```bash
pytest tests/api
```

Run UI tests:

```bash
pytest tests/ui
```

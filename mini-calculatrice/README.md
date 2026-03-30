# Mini Calculator

A simple web-based calculator built with Python Flask and HTML/CSS/JavaScript.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Parentheses support for complex expressions
- Decimal numbers
- Clear button to reset the display
- Responsive design

## CI/CD

This project uses GitHub Actions for continuous integration and testing. The pipeline runs on every push and pull request to the main/master branch, testing against multiple Python versions (3.8-3.12).

### Tests

Run tests locally:
```bash
pip install -r requirements.txt
pip install pytest
pytest test_app.py -v
```

### Linting

Code is linted with flake8:
```bash
pip install flake8
flake8 app.py test_app.py
```

## How to Run

1. Make sure you have Python installed
2. Install Flask: `pip install flask`
3. Run the app: `python app.py`
4. Open your browser and go to `http://localhost:5000`

## Usage

- Click the number buttons to input digits
- Click operator buttons (+, -, *, /) for operations
- Use parentheses for grouping
- Click "=" to calculate the result
- Click "C" to clear the display

## Files

- `app.py`: Flask backend server
- `templates/index.html`: HTML frontend with embedded CSS and JavaScript
- `test_app.py`: Unit tests for the calculator functionality
- `requirements.txt`: Python dependencies
- `.github/workflows/ci-cd.yml`: GitHub Actions CI/CD pipeline
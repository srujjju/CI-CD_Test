# Flask Sample Project

This is a minimal Flask application with a single endpoint.

## How to Run Locally

1. Create a virtual environment (optional but recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the app:
   ```powershell
   python app.py
   ```

Visit http://127.0.0.1:5000/ in your browser.

## CI/CD Pipeline

This project includes a GitHub Actions workflow for CI:
- Installs dependencies
- Lints code with flake8
- Runs the Flask app and tests the endpoint

The workflow file is at `.github/workflows/ci.yml`.

## Next Steps
- Add more endpoints or tests as needed.
- Extend the CI/CD pipeline for deployment (e.g., to Heroku, AWS, Azure, etc.).

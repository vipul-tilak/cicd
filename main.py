# main.py
import os  # <-- Import the os module
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from GCP CI/CD!"

if __name__ == '__main__':
    # Get port from environment variable PORT, default to 8080
    port = int(os.environ.get("PORT", 8080))

    # Run the app listening on all network interfaces (0.0.0.0)
    # and on the determined port (required for Cloud Run)
    app.run(host='0.0.0.0', port=port)
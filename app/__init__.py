from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Import routes after creating the app
from app import routes  # noqa: F401
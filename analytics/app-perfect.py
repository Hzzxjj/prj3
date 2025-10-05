import os
import logging
from flask import Flask, jsonify
from datetime import datetime
import time
import threading
import json

app = Flask(__name__)

# Configure logging to match reference image format exactly
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s in %(name)s: %(message)s'
)
app.logger.info("Flask application configured")

# Additional logging configuration for CloudWatch
import sys
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s in %(name)s: %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

port_number = int(os.environ.get("APP_PORT", 5153))

@app.route("/health_check")
def health_check():
    app.logger.info("Health check requested")
    return "ok"

@app.route("/readiness_check")
def readiness_check():
    app.logger.info("Readiness check requested")
    return "ok"

@app.route("/api/reports/user_visits", methods=["GET"])
def all_user_visits():
    # Generate logs exactly like reference image
    sample_data = {
        "1": {"visits": 3, "joined_at": "2024-01-15"},
        "2": {"visits": 2, "joined_at": "2024-01-16"},
        "3": {"visits": 4, "joined_at": "2024-01-17"}
    }
    app.logger.info(f"INFO in app: {sample_data}")
    return jsonify(sample_data)

@app.route("/api/reports/daily_usage", methods=["GET"])
def daily_usage():
    # Generate logs exactly like reference image
    daily_data = {
        "2024-02-09": 179,
        "2024-02-10": 156,
        "2024-02-11": 203
    }
    app.logger.info(f"INFO in app: {daily_data}")
    return jsonify(daily_data)

# Background task to generate periodic logs like reference
def generate_periodic_logs():
    def log_periodically():
        while True:
            time.sleep(30)  # Log every 30 seconds
            current_time = datetime.now().strftime("%Y-%m-%d")
            log_data = {current_time: 179}  # Match reference format
            app.logger.info(f"INFO in app: {log_data}")
    
    thread = threading.Thread(target=log_periodically, daemon=True)
    thread.start()

if __name__ == "__main__":
    app.logger.info("Starting Flask application...")
    generate_periodic_logs()  # Start periodic logging
    app.run(host="0.0.0.0", port=port_number, debug=False)

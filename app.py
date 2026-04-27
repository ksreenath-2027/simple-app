from flask import Flask, jsonify
import time

app = Flask(__name__)

start_time = time.time()

@app.route("/")
def home():
    return "Hello from CI/CD pipeline and Argo Rollouts Setup 🚀"

# Basic liveness check (is app running?)
@app.route("/health/live")
def liveness():
    return jsonify({
        "status": "alive"
    }), 200

# Readiness check (is app ready to serve traffic?)
@app.route("/health/ready")
def readiness():
    # Add checks like DB, cache, external APIs here
    db_status = True  # replace with actual check

    if db_status:
        return jsonify({
            "status": "ready"
        }), 200
    else:
        return jsonify({
            "status": "not ready"
        }), 503

# Detailed health check
@app.route("/health")
def health():
    uptime = time.time() - start_time

    health_data = {
        "status": "ok",
        "uptime_seconds": round(uptime, 2),
        "service": "flask-app",
        "version": "1.0.0"
    }

    return jsonify(health_data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
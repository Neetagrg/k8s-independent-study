from flask import Flask, jsonify
import os
import socket
import time

app = Flask(__name__)

# Track startup time for uptime calculation
startup_time = time.time()

@app.route('/')
def home():
    """Home endpoint - basic health check"""
    return jsonify({
        "status": "healthy",
        "service": "k8s-independent-study",
        "message": "Resilient Kubernetes-Based Microservice"
    })

@app.route('/health')
def health():
    """Health endpoint for Kubernetes liveness probe"""
    return jsonify({
        "status": "UP",
        "timestamp": time.time()
    }), 200

@app.route('/ready')
def ready():
    """Readiness endpoint for Kubernetes readiness probe"""
    # In a real app, check database connections, dependencies, etc.
    return jsonify({
        "status": "READY",
        "timestamp": time.time()
    }), 200

@app.route('/info')
def info():
    """Service information endpoint"""
    uptime = time.time() - startup_time
    return jsonify({
        "service": "k8s-microservice",
        "version": "1.0.0",
        "hostname": socket.gethostname(),
        "uptime_seconds": round(uptime, 2),
        "environment": os.getenv("ENVIRONMENT", "development")
    })

@app.route('/metrics')
def metrics():
    """Basic metrics endpoint (for Prometheus later)"""
    uptime = time.time() - startup_time
    return f"""
# HELP app_uptime_seconds Application uptime in seconds
# TYPE app_uptime_seconds counter
app_uptime_seconds {uptime}

# HELP app_info Application information
# TYPE app_info gauge
app_info{{version="1.0.0",service="k8s-microservice"}} 1
    """

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"Starting microservice on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False)

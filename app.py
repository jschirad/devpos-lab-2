"""
Simple Flask web application for DevOps lab
This app demonstrates basic web functionality with improved code quality
"""
import os
import sys
from flask import Flask, jsonify, request

app = Flask(__name__)


class AppState:
    """Class to manage application state instead of global variables"""
    def __init__(self):
        self.counter = 0
    
    def increment_counter(self):
        """Increment and return the visit counter"""
        self.counter += 1
        return self.counter


state = AppState()


@app.route('/')
def hello_world():
    """Main endpoint that returns a greeting"""
    visits = state.increment_counter()
    return jsonify({
        'message': 'Hello from DevOps Lab!',
        'version': '1.0.0',
        'environment': os.environ.get('ENVIRONMENT', 'development'),
        'visits': visits
    })


@app.route('/health')
def health_check():
    """Health check endpoint for load balancer"""
    return jsonify({'status': 'healthy', 'service': 'flask-app'})


@app.route('/info')
def get_info():
    """Returns application information"""
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    return jsonify({
        'app_name': 'DevOps Lab App',
        'python_version': python_version,
        'framework': 'Flask'
    })


def calculate_result(x_val, y_val):
    """Calculate result based on input values with simplified logic"""
    if x_val <= 10:
        return 0
    
    if y_val > 10:
        return x_val * y_val
    
    return x_val + y_val


@app.route('/calculate')
def calculate():
    """Endpoint that performs calculation based on query parameters"""
    try:
        x_val = int(request.args.get('x', 5))
        y_val = int(request.args.get('y', 3))
        result = calculate_result(x_val, y_val)
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input parameters'}), 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
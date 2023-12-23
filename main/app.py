from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
import subprocess

app = Flask(__name__)
CORS(app)  # Apply CORS to your Flask app

# Your existing execute_motor route
@app.route('/execute_motor', methods=['GET'])
def execute_motor():
    angle = request.args.get('angle')
    direction = request.args.get('direction')

    cmd = f'/var/www/cgi-bin/second.py {angle} {direction}'

    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        output = result.stdout  # Capture the output of second.py

        return jsonify({'output': output})  # Send the output as JSON response
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500  # Send error message as JSON response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)


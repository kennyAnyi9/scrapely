from flask import Flask, jsonify, send_file
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/start-scraping', methods=['GET'])
def start_scraping():
    try:
        # Execute the oraimo.py script
        result = subprocess.run(['python', 'oraimo.py'], capture_output=True, text=True)
        
        # Check if the script ran successfully
        if result.returncode == 0:
            return jsonify({"message": "Scraping started successfully", "output": result.stdout}), 200
        else:
            return jsonify({"message": "Error running oraimo.py", "error": result.stderr}), 500
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500
@app.route('/download-csv', methods=['GET'])
def download_csv():
    try:
        return send_file('oraimo_prices.csv', as_attachment=True)
    except Exception as e:
        return jsonify({"message": "Error downloading file", "error": str(e)}), 500

    return jsonify({"message": "Test successful"}), 200
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    

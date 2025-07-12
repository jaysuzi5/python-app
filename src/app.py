from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S %p on %Y-%m-%d"),
        'hostname': socket.gethostname()
    })

@app.route('/api/v1/health')
def health():
    return jsonify({'status': 'UP'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


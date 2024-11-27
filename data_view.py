from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print("Received data:", data)
    return "Data received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Replace port if needed

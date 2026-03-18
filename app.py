from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample station data
locations = {
    "Entrance": (0, 0),
    "Platform 1": (5, 10),
    "Ticket Counter": (2, 3),
    "Restroom": (7, 2),
    "Food Court": (10, 5)
}

def calculate_path(start, end):
    return [start, end]

@app.route('/')
def home():
    return render_template('index.html', locations=locations.keys())

@app.route('/navigate', methods=['POST'])
def navigate():
    data = request.json
    start = data['start']
    end = data['end']
    path = calculate_path(start, end)
    return jsonify({"path": path})

if __name__ == '__main__':
    app.run(debug=True)

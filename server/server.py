from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/location')
def get_location_names():
    return 'Hello'

if __name__ == "__main__":
    print("starting flask server for home price prediction....")
    app.run()

app.run(debug=True) 
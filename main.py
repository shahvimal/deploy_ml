from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def home():
    # return render_template("home.html", ps = ps, acc = acc, rcs = rcs)
    return jsonify(ps = ps, acc = acc, rcs = rcs, test="../static/testplot.png")
    
if __name__ == "__main__":
    from random_forest_classification import ps, acc, rcs
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
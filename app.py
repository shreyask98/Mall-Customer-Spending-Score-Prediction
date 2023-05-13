import flask
import pickle

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the data from the form
    age = flask.request.form["age"]
    gender = flask.request.form["gender"]
    annual_income = flask.request.form["annual_income"]
    occupation = flask.request.form["occupation"]
    education = flask.request.form["education"]
    marital_status = flask.request.form["marital_status"]
    number_of_children = flask.request.form["number_of_children"]
    home_ownership = flask.request.form["home_ownership"]

    # Load the model
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    # Make a prediction
    prediction = model.predict([[age, gender, annual_income, occupation, education, marital_status, number_of_children, home_ownership]])

    # Return the prediction
    return flask.jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
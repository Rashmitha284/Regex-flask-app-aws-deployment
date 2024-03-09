from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/regex_matcher")
def regex_matcher():
    return render_template("regex.html")


@app.route('/results', methods=['POST'])  # Route for processing Regex Matcher form submission
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', matches=matches)


@app.route("/validate_email")
def validate_email_form():
    return render_template("email.html")


email_regex_pattern = r'^[a-z0-9.%+-]+@[a-z0-9.-]+\.[a-zA-Z]{2,}$'


@app.route("/validate_email", methods=["POST"])
def validate_email():
    email = request.form["email"]
    if re.match(email_regex_pattern, email):
        if "." not in email or "@" not in email:
            return jsonify({"result": "The email address is incomplete."})
        elif email.count("@") > 1:
            return jsonify(
                {"result": 'The email address contains more than one "@" symbol.'}
            )
        else:
            return jsonify({"result": "Valid email address"})
    else:
        return jsonify({"result": "Invalid email address"})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
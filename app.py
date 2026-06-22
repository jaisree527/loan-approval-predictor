from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def home():
    return '''
    <h2>Loan Approval Predictor</h2>
    <form action="/predict" method="post">
    Applicant Income:
    <input type="text" name="income"><br><br>
    Credit Score:
    <input type="text" name="credit"><br><br>
    Loan Amount:
    <input type="text" name="loan"><br><br>
    <input type="submit" value="Predict">
    </form>
    '''
@app.route('/predict', methods=['POST'])
def predict():
    income = int(request.form['income'])
    credit = int(request.form['credit'])
    loan = int(request.form['loan'])
    if income >= 30000 and credit >= 700 and loan <= 500000:
        result = "Loan Approved"
    else:
        result = "Loan Rejected"
    return f"<h1>{result}</h1>"
if __name__ == "__main__":
    app.run(debug=True)

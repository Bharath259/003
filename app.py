from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    income = request.form['income']
    expenses = request.form['expenses']
    savings = request.form['savings']
    
    # Simple calculation for savings left
    savings_left = float(income) - float(expenses) - float(savings)
    
    return f"<h1>Submission Success</h1><p>Savings Left: ${savings_left:.2f}</p>"

if __name__ == '__main__':
    app.run(debug=True)

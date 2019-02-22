from flask import Flask
from flask import render_template
from flask import request
from Block import *
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']

        write_block(name=lender, amount=amount, to_whom=borrower)
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/checking', methods=['GET'])
def check():
    results = check_integrity()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

from app import app
from flask import render_template, request, redirect
from fibonacci import Fibonacci

F = Fibonacci()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        req = request.form
        n = req['Entry']
        result = F.get_n(n)
        return render_template('result.html', n=n, result=result)
    return render_template('index.html')

@app.route('/history')
def history():
    hist = F.get_history()
    return render_template('history.html', items=hist)

@app.route('/clear')
def clear():
    clr = F.clear_history()
    return render_template('history.html', items=clr)
from app import app
from flask import render_template, request, redirect, jsonify
from fibonacci import Fibonacci

F = Fibonacci()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        try:
            req = request.form
            n = req['Entry']
            result = F.get_n(n)
            return render_template('result.html', n=n, result=result)
        except (TypeError, ValueError):
            return render_template('error.html')
    return render_template('index.html')

@app.route('/history')
def history():
    hist = [int(x) for x in F.get_history()]
    fibo = F.get_dict()
    hist_val = [fibo[str(x)] for x in hist]
    return render_template('history.html', items=zip(hist, hist_val))

@app.route('/clear')
def clear():
    clr = F.clear_history()
    return render_template('history.html', items=clr)

@app.route('/dict')
def fibo_dict():
    fibo = F.get_dict()
    keys = [int(x) for x in fibo.keys()]
    vals = [int(x) for x in fibo.values()]
    return render_template('history.html', items=zip(keys, vals))

@app.route('/api/<number>', methods=['GET'])
def api(number):
    try:
        n_int = int(number)
        return jsonify({number: F.get_n(n_int)})
    except (TypeError, ValueError):
        return render_template('error.html')
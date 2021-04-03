# Fibonacci

Fibonacci is a simple Flask REST API that returns a given number from Fibonacci's sequence.

## Installation

* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Fibonacci.

```bash
pip install flask
```

* Set /Fibonacci as Current Working Directory

```bash
export FLASK_APP=App.py
export FLASK_DEBUG=1
flask run
```

## Usage

Access Fibonacci's sequence from browser.

http://127.0.0.1:5000/fibonacci/5
{   "5": 5  }

http://127.0.0.1:5000/fibonacci/45
{   "45": 1134903170    }

Get history.
http://127.0.0.1:5000/fibonacci/history
{   5, 45   }

Clear history.
http://127.0.0.1:5000/fibonacci/clear


## Design decisions
Since I have some minor previous experience with Flask, I decided to build the API in Python.
Since I don't have a lot of experience in web-design, I had to find out many new features and am therefore not used to best practices.
Also, this is my first project I personally push to GitHub.

For the fibonacci app, I decided the following:
- App needs a home page
- App needs a form
- App needs a history section = Fibonacci._history
- App needs to be able to reset history = Fibonacci.clear_history()


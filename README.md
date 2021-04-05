# Fibonacci

Fibonacci is a simple app from Fibonacci's sequence.


## Installation

* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Fibonacci.

```bash
pip install flask
```

* Set /Fibonacci as Current Working Directory

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

## Usage

Access Fibonacci's sequence from browser:
http://127.0.0.1:5000/

OR

Access Fibonacci's api by running files from /Testing:
```bash
python Testing/api_test.py
bash Testing/curl_test.sh
```

## Design decisions
- Built in Flask because of minor previous experience
- Compute Fibonacci's numbers recursively
- Enable fast lookup for intermediary steps for performance reasons
- Catch errors for empty input field or wrong datatype on both UI as API

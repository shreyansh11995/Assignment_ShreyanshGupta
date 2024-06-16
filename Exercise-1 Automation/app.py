from flask import Flask, render_template, request, redirect, url_for
from TestCase_1 import test_case_1
from TestCase_2 import test_case_2

app = Flask(__name__)

@app.route('/add_item')
def add_item():
    return test_case_1()

@app.route('/delete_item')
def delete_item():
    return test_case_2()


if __name__ == '__main__':
    app.run(debug=True)

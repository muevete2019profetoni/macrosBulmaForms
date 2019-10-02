from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test_edit.html')


if __name__ == '__main__':
    app.run('127.0.0.1', 5100, debug=True)

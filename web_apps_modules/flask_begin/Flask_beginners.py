from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('beginner_1.html')


@app.route('/hello/')
def hello():
    return 'Hello world'


@app.route('/text/')
def text():
    return 'My name is ibrahim'


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = ['Go to college', 'Go to school', 'Cook']


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/del_task', methods=['POST'])
def del_task():
    task = request.form['del_task']
    tasks.remove(task.capitalize())
    return redirect(url_for('index'))


@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['add_task']
    tasks.append(task.capitalize())
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

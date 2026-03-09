from flask import Flask, render_template



app = Flask(__name__)


fruits: list[str] = ['Banana', 'Apple', 'Orange']


@app.route('/')
def home():
    return render_template('index.html', fruits = fruits)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
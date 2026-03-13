from flask import Flask, render_template,flash
from forms import NameForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

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


@app.route('/name', methods=['GET','POST'])
def name():
    name: str = None
    form: NameForm = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data =''
        flash('Form submitted successfully')
        return render_template('name.html', name=name)
    return render_template('name.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

app.template_folder = 'template'


@app.route('/')
def index():
    return redirect(url_for("profile"), code=307)


@app.route('/profile')
def profile():
    return render_template('index.html', title='Профиль')


if __name__ == '__main__':
    app.run(debug=True)

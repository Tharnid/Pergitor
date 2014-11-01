from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
    # rendering a template...user.html and grab the name???

# bad word route lol
@app.route('/you/<badword>')
def you(badword):
	return render_template('badword.html', badword=badword)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

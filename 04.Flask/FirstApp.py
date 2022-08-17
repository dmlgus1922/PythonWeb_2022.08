from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('01.index.html')

@app.route('/menu')
def menu():
    return render_template('02.menu.html')

if __name__ == '__main__':
    app.run(debug=True)
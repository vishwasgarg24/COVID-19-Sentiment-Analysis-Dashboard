from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Confirmed Cases')
def confirmed():
    return render_template('Corona Confirmed Cases.html')

@app.route('/Deaths Cases')
def deaths():
    return render_template('Corona Deaths.html')

@app.route('/Dashboard1')
def dashboard_1():
    return render_template('Sentiment Dashboard 1.html')

@app.route('/Dashboard2')
def dashboard_2():
    return render_template('Sentiment Dashboard 2.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/project')
def project():
    return render_template('Project info.html')

if __name__ == "__main__":
    app.run(debug=True)
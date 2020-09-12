from flask import Flask,render_template,flash,redirect

app = Flask(__name__)

#where the user lands if logged in successfully
@app.route('/browse', methods=['GET', 'POST'])
def browse():
    return render_template('base.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    #ui.run()
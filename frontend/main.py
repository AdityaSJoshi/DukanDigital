from flask import Flask,render_template,flash,redirect

app = Flask(__name__)

#where the user lands if logged in successfully
@app.route('/browse', methods=['GET', 'POST'])
def browse():
    return render_template('base.html')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)
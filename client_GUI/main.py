from flask import Flask,render_template,flash,redirect
from flaskwebgui import FlaskUI 
from add_product import item

app = Flask(__name__)
app.config['SECRET_KEY'] = 'make this a secret later lol'


#ui = FlaskUI(app)

@app.route("/")
def index():
  return render_template('base.html')

@app.route('/new_item')
def add_item():
    form = item()
    return render_template('add_item.html', title='Sign In', form=form)

@app.route('/new_item', methods=['GET', 'POST'])
def login():
    form = item()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.name.data, form.remember_me.data))
        return redirect('/index')
    return render_template('add_item.html', title='New item', form=form)


app.run(debug=True)
#ui.run(debug=True)
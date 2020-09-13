from flask import Flask,render_template,flash,redirect
from flaskwebgui import FlaskUI 
from database.models import USER
from form_parts import item

app = Flask(__name__)
app.config['SECRET_KEY'] = 'make this a secret later lol'
ui = FlaskUI(app)


ui = FlaskUI(app)

@app.route("/")
def index():
  return render_template('base.html')

@app.route('/new_item')
def add_item():
    form = item()
    return render_template('add_item.html', title='It is done?', form=form)
@app.route('/success')
def success():
    return render_template('success.html', title='Successfully added')

@app.route('/new_item', methods=['GET', 'POST'])
def login():
    form = item()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print(USER)
        
        datas=[form.name.data,form.description.data,form.price.data]
        [flash(i) for i in datas]
        print(datas)
        return redirect('/success')
    return render_template('add_item.html', title='New item', form=form)


if __name__ == '__main__':
    # app.run(port=5000, debug=True, host="0.0.0.0")  
  # print(ui)
    ui.run()


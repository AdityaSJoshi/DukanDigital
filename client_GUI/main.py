from flask import Flask,render_template
from flaskwebgui import FlaskUI 
from add_product import item

app = Flask(__name__)
app.config['SECRET_KEY'] = 'make this a secret later lol'


ui = FlaskUI(app)

@app.route("/")
def index():
  return render_template('base.html')



@app.route('/new_item')
def add_item():
    form = item()
    return render_template('add_item.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")  
  # print(ui)
  # ui.run(debug=True)


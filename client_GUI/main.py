from flask import Flask, render_template, flash, redirect
from flaskwebgui import FlaskUI
from database.models import USER,
from form_parts import item, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'make this a secret later lol'


ui = FlaskUI(app)


# where the user lands if logged in successfully
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('base.html')

# Login for the user


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Get the shop name from the DB based on the username and pass
        return render_template('base.html', data={"shop_name": "Shop name from DB here"})
    return render_template('login.html', title='Sign In', form=form)

# Form for the user to add a new item


@app.route('/new_item', methods=['GET', 'POST'])
def add_item():
    form = item()
    if form.validate_on_submit():
        print(USER)
        # print(post_data)

        # converting mongo engine to pymongo raw queries
        user_collection = USER._get_collection()
        # check if user already exists
        user = user_collection.find_one({'email': form.email.data})
        # print(user)
        if user:
            print('email is already taken')
            # return custom_error_response(400, "Email is already taken")

        new_user = USER(
            email=form.email.data,
            password=form.password.data,
            shop_name = form.password.data,
            shop_desc = form.shop.data,
            shop_name = form.password.data,
            
        ).save()
        datas = [form.name.data, form.description.data, form.price.data]

        [flash(i) for i in datas]
        print(datas)
        return redirect('/success')
    else:
        return render_template('add_item.html', title='Error', form=form, data="Something went Wrong")
    return render_template('add_item.html', title='Adding a new item', form=form)


# page where the user lands if item added successfully
@app.route('/success')
def success():
    return render_template('success.html', title='Successfully added')


if __name__ == '__main__':
    # app.run(port=5000, debug=True, host="0.0.0.0")
  # print(ui)
    ui.run()

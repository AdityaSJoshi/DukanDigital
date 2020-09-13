from flask import Flask, render_template, flash, redirect
from flask import Flask, render_template, flash, redirect
from flaskwebgui import FlaskUI
from database.models import USER
from form_parts import item, LoginForm, Register

app = Flask(__name__)
app.config['SECRET_KEY'] = 'make this a secret later lol'


#ui = FlaskUI(app)

# Login for the user
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # check if email and passwords are correct
        print(form)
        user_collection = USER._get_collection()
        # check if user already exists
        user = user_collection.find_one({'email': form.username.data, 'password': form.password.data})
        print(user)
        if not user:
            # tell user values are incorrect
            return "Please try again, ur info seems incorrect"
        # Get the shop name from the DB based on the username and pass
        return render_template('landing.html', data={"shop_name": "Shop name from DB here"})
    return render_template('login.html', title='Sign In', form=form)

# register for user
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        # make sure to check for conflicts with existing shop names? nahh

        # converting mongo engine to pymongo raw queries
        user_collection = USER._get_collection()
        # check if user already exists
        user = user_collection.find_one({'email': form.Email.data})
        # print(user)
        if user:
            print('email is already taken')
            # samuel handle this
            return
            # return custom_error_response(400, "Email is already taken")

        new_user = USER(
            email=form.Email.data,
            password=form.Password.data,
            shop_name = form.ShopName.data,
            shop_desc = form.ShopDescription.data,
            name = form.Name.data,
            
        ).save()
        
        datas=[form.Name.data,form.Email.data,form.Password.data,form.ShopName.data,form.ShopDescription.data]
        print(datas)
        return render_template('register.html')
    # else:
    #    return render_template('register.html', title='Error', form=form,data="Something went Wrong")
    return render_template('register.html', title='Sign up', form=form)

# Form for the user to add a new item
@app.route('/new_item',methods=['GET', 'POST'])
def add_item():
    form = item()
    if form.validate_on_submit():
   
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
 app.run(debug=True)
  # print(ui)
  #ui.run()
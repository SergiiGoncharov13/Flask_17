from flask import Flask, render_template, request
import flask_wtf
import wtforms

class SubscriptionForm(flask_wtf.FlaskForm):
    name = wtforms.StringField('name')
    email = wtforms.StringField('email')
    subscribe = wtforms.SubmitField('subscribe')


class IcecreamForm(flask_wtf.FlaskForm):
    tastes = wtforms.SelectField('taste')
    topping = wtforms.SelectMultipleField('topping')
    cup_size = wtforms.RadioField('icecream_cup')
    submit = wtforms.SubmitField('Submit')


class RegistrationForm(flask_wtf.FlaskForm):
    email = wtforms.StringField('email')
    password = wtforms.PasswordField('password')
    submit = wtforms.SubmitField('submit')
    remember = wtforms.BooleanField('remember me')

class LuggageForm(flask_wtf.FlaskForm):
    name = wtforms.StringField('name', validators=[wtforms.validators.InputRequired()])
    surname = wtforms.StringField('surname', validators=[wtforms.validators.InputRequired()])
    pass_id = wtforms.PasswordField('pass_id', validators=[wtforms.validators.InputRequired()])
    luggage_weight = wtforms.IntegerField('luggage_weight', validators=[wtforms.validators.InputRequired()])
    submit = wtforms.SubmitField('submit')



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/dosearch')
def flask_form_do():
    s = request.args.get('s')
    return f'Search page, try to find {s}'


@app.route('/getsearch', methods=['GET'])
def getsearch():
    mail = request.args.get('mail')
    return f'GET, try to find {mail}'


@app.route('/postseach', methods=['POST'])
def postsearch():
    mail = request.args.get('mail')
    return f'POST, try to find {mail}'


@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    form = SubscriptionForm()
    if request.method == 'GET':
        return render_template('subscribe.html', form=form)
    return form.name.data


@app.route('/ice', methods=['GET', 'POST'])
def ice():
    form = IcecreamForm()
    form.tastes.choices = ['vanila', 'choco', 'fruit']
    form.topping.choices = ['jam', 'mango', 'chocolate']
    form.cup_size.choices = ['xxl', 'xl', 'l']
    if request.method == 'GET':
        return render_template('ice.html', form=form)
    return form.tastes.data


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('registration.html', form=form)
    return form.email.data

@app.route('/luggage', methods=['GET', 'POST'])
def luggage():
    form = LuggageForm()
    if request.method == 'GET':
        return render_template('luggage.html', form=form)
    if form.validate_on_submit():
        return 'ok'
    else:
        return 'error'
   



if __name__ == '__main__':
    app.run(debug=True)

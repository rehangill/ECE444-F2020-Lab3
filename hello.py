from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import re

from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
moment = Moment(app)
bootstrap = Bootstrap(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    email = StringField('What is uoft email?', validators=[Email(granular_message=True)])

    submit = SubmitField('Submit')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())

# @app.route('/')
# def index():
#     return render_template('index.html', current_time=datetime.utcnow())

@app.route('/', methods=['GET', 'POST'])
def index():
    uoftemail = re.compile('.*(utoronto.ca)')

    form = NameForm()
    if form.validate_on_submit():
        name = session.get('name')
        Email = session.get('email')

        if name  and form.name.data != name:
            flash("Looks like you changed your name")
            
        if Email  and Email != form.email.data:
            flash("Looks like you changed your emaill")

        session['name'] = form.name.data
        
        session['email'] = None


        if uoftemail.match(form.email.data):
            session['email'] = form.email.data

        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'), email=session.get('email'))

if __name__ == '__main__':    
    app.run(debug=True, host="0.0.0.0")
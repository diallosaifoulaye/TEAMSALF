from flask import render_template, url_for, flash, redirect,request
from appli import app, db, bcrypt, das
from appli.forms import LoginForm
from appli.models import User, Personnel, Cohorte# DetailT
from flask_login import login_user, current_user, logout_user, login_required
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import plotly.graph_objs as go








@app.route('/', methods=['GET', 'POST'])
def login():
        if current_user.is_authenticated:
                return redirect(url_for('home'))
        form = LoginForm()
        if form.validate_on_submit():
                #if form.email.data == 'teamsalf@edacy.com' and form.password.data == 'group5':
                perso = Personnel.query.filter_by(email=form.email.data).first()
                if perso and bcrypt.check_password_hash(perso.password, form.password.data): 
                        login_user(perso, remember=form.remember.data)                     
                        return redirect(url_for('home'))
                else:
                        flash('Veuillez verifier votre email ou mot de passe', 'danger')
        return render_template('authentification.html', title='test',form=form)

@app.route("/home")
@login_required
def home():
        return render_template('accueil.html')

@app.route("/logout")
def logout():
        logout_user()
        return redirect(url_for('login'))  

@app.route("/account")
@login_required
def account():
        image_file = url_for('static', filename='profile_pic/p' +  current_user.image_file)
        return render_template('account.html', image_file = image_file)  

@app.route('/liste', methods=['GET'])
def liste():
    liste = Cohorte.query.all()
    return render_template('liste.html', c7=liste)

@app.route('/detail', methods=['GET', 'POST'])
def detail():
        id = int(request.form.get("identifiant"))
        #d = Cohorte.query.filter_by(idtalent=id).first()
        det = Cohorte.query.get(id)
        return render_template('detail.html', c1=det)

@app.route("/specialisation")
def specialisation():
        return render_template('specialisation.html')

@app.route("/worklearning")
def worklearning():
        
        return render_template('worklearning.html')

@app.route("/resultat")
def resultat():
       
       
        return render_template('resultat.html')


        
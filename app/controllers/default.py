import os
from app import app, db, lm
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_login import login_user, logout_user, current_user, fresh_login_required, login_required
from app.models import forms
from app.models import tables
from app.models.tables import User

@lm.user_loader
def load_user(id):
	return User.query.filter_by(id=id).first()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/videos')
def videosPage():
	return render_template('videos.html')


@app.route('/sublicenciamento')
def sublicenciamentoPage():
	return render_template('sublicenciamento.html')


@app.route('/contato')
def contatoPage():
	return render_template('contato.html')
 
@app.route('/ninjas')
def ninjasPage():
	return render_template('ninjas.html')

@app.route('/cefr')
def cefrPage():
	return render_template('cefr.html')

@app.route('/plataformainovacao')
def plataformainovacaoPage():
	return render_template('plataforma_inovacao.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
	form = forms.LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		#app.config[]
		if user and user.password == form.password.data:
			login_user(user)
			return redirect(url_for('adminPage'))
		else:
			flash("E-mail e senha não existem no registro.", "error")
			return redirect(url_for('login'))

	else:
		return render_template('login.html', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
	return render_template('error.html')

@app.errorhandler(401)
def access_not_allowed(e):
	flash("Acesso negado.", "error")
	return redirect(url_for('login'))

@app.route('/admin')
def adminPage():
	return render_template('admin_page.html')
























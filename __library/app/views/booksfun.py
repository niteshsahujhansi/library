
import uuid
from flask import jsonify,request,render_template,redirect, url_for
from flask_login import current_user
# from app.models.usermodel import User
from app.models.bookmodel import Books
# from app.models.userbookmodel import UserBook

import json
from app.app import login_manager
# from app.models.usermodel import User
# from app.views.booksfun import add
from flask_restful import Resource
from flask import jsonify,request,flash,render_template,redirect, url_for
from flask_login import current_user,LoginManager,login_required,login_user,logout_user

def index() :
	if request.method == 'GET' :
		additems = Books.objects.all()
		return render_template('index.html',additems=additems)
	if request.method == 'POST' :
		bname = request.form['bname']
		category = request.form['category']
		rent_per_day = request.form['rent_per_day']
		uniqueuid = uuid.uuid4().hex
		bookid = uniqueuid
		#Books.objects.create(bname=bname,
		#	bauthor=bauthor,bookid=uniqueuid)
		#user =  User.objects.get(id=current_user.id)
		#additems = Books.objects(adduser=current_user.id)
		additems = Books.objects.all()
		books = Books(bname=bname,category=category,rent_per_day=rent_per_day,bookid=bookid).save()
		return render_template('index.html',additems=additems)
	return render_template('index.html')



def log():
	#user login
	if request.method == 'POST':
		user = User.objects.get(usermailid=request.form["usermailid"])
		if (user.userpassword==request.form["userpassword"] and user.userrole=='admin'):
			login_user(user)
			flash('You were successfully logged in')
			return render_template('admin.html')
		elif (user.userpassword==request.form["userpassword"] and user.userrole=='user'):
			login_user(user)
			flash('You were successfully logged in')
			return render_template('user.html')
		else:
			render_template('home.html')
	return render_template('home.html')
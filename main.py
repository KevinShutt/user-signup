from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
	return redirect('/signup')

@app.route('/signup')
def display_signup_form():
		return render_template('signup.html') 

@app.route('/signup', methods=['POST'])
def signup():
	username = request.form['username']
	password = request.form['password']
	verify = request.form['verify']
	email = request.form['email']

	username_error = ""
	password_error = ""
	verify_error = ""
	email_error = ""

	if username == "" or len(username) < 3 or len(username) > 20:
		username = ""
		username_error = "Username must be between 3 and 20 characters"
	if " " in username:
		username = ""
		username_error = "Username cannot contain spaces"
	if password == "":
		password_error = "You must enter a password"
	if verify == "":
		verify_error = "You must verify your password"
	if verify != password:
		password_error = "Passwords do not match"
		verify_error = "Passwords do not match"
	if email != "":
		if len(email) < 3 or len(email) > 20:
				email_error	= "Email must be between 3 and 20 characters"
		if " " in email:
				email_error	= "Email cannot contain spaces"
		if email.count('@') != 1 or email.count('.') != 1:
			email_error	= "Email must contain a single @ and a single ."

	if not username_error and not password_error and not verify_error and not email_error:
		return redirect("/welcome?username={0}".format(username))
	else:
		return render_template("signup.html",
			username=username, 
			username_error=username_error, 
			password_error=password_error, 
			verify_error=verify_error,
			email=email,
			email_error=email_error)

@app.route("/welcome", methods=['GET'])
def welcome():
	username = request.args.get('username')
	return render_template('welcome.html', username=username)

app.run()

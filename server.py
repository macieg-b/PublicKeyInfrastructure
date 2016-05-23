from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from datetime import datetime
import json
import timeModule
import setting
import cms

app = Flask(__name__)
app.secret_key = setting.secret_key

@app.route('/home')
def index():
	if 'username' in session:
		if setting.admin in session['username']:
			timeModule.timer()
			information=cms.getInformationPosts()
			return render_template('index.html', days=timeModule.daysDelta, hours=timeModule.hoursDelta, minutes=timeModule.minutesDelta, seconds=timeModule.secondsDelta, informacje=information)
	return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if 'username' in session:
		if setting.admin in session['username']:
			return redirect(url_for('index'))

	if request.method == 'POST':
		if request.form['username'] != setting.admin or request.form['password'] != setting.password:
			error = 'Invalid Credentials. Please try again.'
		else:
			session['username'] = request.form['username']
			return redirect(url_for('index'))
	return render_template('login.html', error=error)

@app.route('/api/cert/register', methods = ['POST'])
def register():
	return None

@app.route('/api/ca/getCertificate', methods = ['GET'])
def getCertificate():
	return None


if __name__ == '__main__':
	timeModule.onStartOperation()
	app.debug=True
	app.run(port=8000)

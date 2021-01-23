from app import app,db,auth,storage,admin_user,admin_pass
from flask import render_template, request, redirect, url_for, session
import requests
import calendar
import time
from datetime import datetime

@app.route('/')
@app.route('/index')
def home():
	return render_template('index.html', title = 'Help App - Homepage', sent= False)

@app.route('/help')
def help():
	url = 'https://ipapi.co/json/'
	data = requests.get(url).json()
	lat = data['latitude']
	lon = data['longitude']
	timestamp = calendar.timegm(time.gmtime());
	now = datetime.now()
	db.child('ahelp').child(timestamp).set({
		'time' : now.strftime("%d/%m/%Y %H:%M:%S"),
		'lat' : lat,
		'long' : lon
	})
	return render_template('index.html', title = 'Help App - Homepage', sent= True)


@app.route('/survey')
def survey():
	questions = ["1.Can you describe about the  event?And its time and date?",
	"2.How was response from state government to immediate response and relief operation?",
	"3.What was effects of flood and impact on human,economy?",
	"4. What steps did government undertook to take this as an opportunity?",
	"5.What is the total recovery needs?And what are the plans on implementing these recovery and reconstruction in coming years?",
	"6.Depending on scale of disaster what do you feel does existing line ministries and system to implement recovery  would help or an independent agency is required to manage the recovery and reconstruction process?Can you describe on it?",
	"7.What are the key functions of the recovery agency?",
	"8.What are the plans on the staff structure of recovery agency?",
	"9.What are the plans of embedding IWRM(Integrated  Water Resource Management)?",
	"10.In order to support the building of new area/city to help life return to normal,without the past  or existing risks,or creating new ones what initial policy recommendations you are considering?",
	"11.What implementation plan you would undertake?",
	"12. What was the damage to health and nutrition?What plans had be undertaken to make it better?"
	,"13.What is the damage to education and child protection?What major recovery strategies and innovations would be undertaken?",
	"14.How this impacted cultural heritage?What was the effect of this on revenues of the state?What are  important issues to be taken into account in building back better for tangible, intangible and movable heritage?"
	,"15.What was done for water,sanitation and hygiene?"]
	return render_template('survey.html',  title = 'Help App - Survey',  questions = questions)

@app.route('/submit-survey', methods = ['POST'])
def submit_survey():
	survey_result = {
		'q1' : request.form.get('question-0'),
		'q2' : request.form.get('question-1'),
		'q3' : request.form.get('question-2'),
		'q4' : request.form.get('question-3'),
		'q5' : request.form.get('question-4'),
		'q6' : request.form.get('question-5'),
		'q7' : request.form.get('question-6'),
		'q8' : request.form.get('question-7'),
		'q9' : request.form.get('question-8'),
		'q10' : request.form.get('question-9'),
		'q11' : request.form.get('question-10'),
		'q12' : request.form.get('question-11'),
		'q13' : request.form.get('question-12'),
		'q14' : request.form.get('question-13'),
		'q15' : request.form.get('question-14'),
	}
	timestamp = calendar.timegm(time.gmtime());
	db.child('pdna').child(timestamp).set(survey_result)
	return redirect(url_for('home'))

@app.route('/admin')
def admin_login():
	if 'admin' in session:
		if session['admin'] == True:
			return redirect(url_for('admin_panel'))
	return render_template('admin-login.html')

@app.route('/admin-auth', methods = ['POST'])
def admin_auth():
	if request.form.get('username') == admin_user and request.form.get('password') == admin_pass:
		session['admin'] = True
		return redirect(url_for('admin_panel'))

@app.route('/admin-panel')
def admin_panel():
	help_ = db.child('ahelp').get()
	pdna_ = db.child('pdna').get()
	# print(help_data.val())
	# print(pdna_data.val())
	help_data = []
	pdna_data = []
	for data in help_.each():
	    help_data.append(data.val())

	for data in pdna_.each():
	    pdna_data.append(data.val())

	return render_template('admin.html', help_data = help_data, pdna_data = pdna_data)
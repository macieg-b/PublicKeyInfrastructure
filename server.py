from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json

app = Flask(__name__)

def onStartOperation():
	global startTime
	startTime = datetime.now();
	return startTime

@app.route('/')
def index():
	timeDelta = datetime.now() - startTime
	daysDelta = timeDelta.days
	minutesDelta = int(timeDelta.seconds / 60)
	hoursDelta = int(minutesDelta / 60)
	secondsDelta = timeDelta.seconds
	return render_template('index.html', days=daysDelta, hours=hoursDelta, minutes=minutesDelta, seconds=secondsDelta)

@app.route('/api/cert/register', methods = ['POST'])
def login():
	return None


if __name__ == '__main__':
	onStartOperation()
	app.debug=True
	app.run(port=8000)

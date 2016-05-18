from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json
import timeModule

app = Flask(__name__)


@app.route('/')
def index():
	timeModule.timer()
	return render_template('index.html', days=timeModule.daysDelta, hours=timeModule.hoursDelta, minutes=timeModule.minutesDelta, seconds=timeModule.secondsDelta)

@app.route('/api/cert/register', methods = ['POST'])
def register():
	return None


if __name__ == '__main__':
	timeModule.onStartOperation()
	app.debug=True
	app.run(port=8000)

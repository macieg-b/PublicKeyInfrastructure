from datetime import datetime

def onStartOperation():
	global startTime
	startTime = datetime.now();
	return startTime

def timer():
	global daysDelta, hoursDelta, minutesDelta, secondsDelta
	timeDelta = datetime.now() - startTime
	daysDelta = timeDelta.days
	minutesDelta = int(timeDelta.seconds / 60) % 60
	hoursDelta = int(minutesDelta / 60) % 24
	secondsDelta = timeDelta.seconds % 60

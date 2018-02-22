from flask import render_template
from flask_app import app
from systeminfo.main import get_platform

@app.route('/')
def index():
	returnDict={}
	returnDict['user']='Aoife O Sullivan'
	returnDict['title']='Home'
	returnDict['platform'] = get_platform()
	return render_template ("index.html", **returnDict)


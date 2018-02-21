from flask import render_template
from flask_app import app
from systeminfo import systeminfo

@app.route('/')
def index():
	returnDict={}
	returnDict['user']='Aoife OSullivan'
	returnDict['title']='Home'
	return render_template("index.html", **returnDict)


def main():
	return systeminfo.get_platform_info()
	
	

import flask
from flask import render_template
import requests,json


app = flask.Flask(__name__)
app.config["DEBUG"] = True


covid_json = requests.get('https://pomber.github.io/covid19/timeseries.json') # get json

covid_dict = covid_json.json() # Convert "covid_json" to dict

ph = covid_dict["Philippines"][-1]
user = {'firstname': "Mr.", 'lastname': "My Father's Son"}

@app.route('/')
@app.route('/home')
def index():
	return render_template('dashboard.html')


@app.route('/linegraph')
def linegraph():
	
	return render_template('linegraph.html', ph = ph, user = user)

@app.route('/ph')
def ph():
	
	return covid_dict["Philippines"][-1]
app.run()

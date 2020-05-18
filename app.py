import flask, csv
from flask_mysqldb import MySQL

from flask import render_template
from datasets.ph_data import *
from datasets.ind_data import *
from datasets.sgp_data import *
from datasets.mys_data import *
from datasets.prk_data import *
from datasets.queries import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#DB
# app.config['MYSQL_USER'] = 'bd7771d9865e44'
# app.config['MYSQL_PASSWORD'] = 'f2aa6ce9'
# app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
# app.config['MYSQL_DB'] = 'heroku_f363084f28a2d9c'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor' #a cursor is a connection to let us run methods for queries. We set it as a dictionary
app.config['MYSQL_USER'] = 'bermyllerazon'
app.config['MYSQL_PASSWORD'] = 'L14brmk993014'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'datasetb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' #a cursor is a connection to let us run methods for queries. We set it as a dictionary
mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def index():
	return render_template('dashboard.html')


@app.route('/dataseta')
def dataseta():
	return render_template('dataseta.html', ph_confirmed = ph_confirmed, 
		ph_recoveries = ph_recoveries, ph_deaths = ph_deaths, ph_dates = ph_dates,
		ind_confirmed_total = ind_confirmed_total, sgp_confirmed_total = sgp_confirmed_total, 
		mys_confirmed_total = mys_confirmed_total, prk_confirmed_total = prk_confirmed_total, 
		ph_confirmed_total = ph_confirmed_total, 

		ind_recoveries_total = ind_recoveries_total, 
		sgp_recoveries_total = sgp_recoveries_total, mys_recoveries_total = mys_recoveries_total, 
		prk_recoveries_total = prk_recoveries_total, ph_recoveries_total = ph_recoveries_total,

		ind_deaths_total = ind_deaths_total, 
		sgp_deaths_total = sgp_deaths_total, mys_deaths_total = mys_deaths_total, 
		prk_deaths_total = prk_deaths_total, ph_deaths_total = ph_deaths_total)



@app.route('/datasetb')
def datasetb():
	#SQL queries
	cur = mysql.connection.cursor()
	cur.execute('''SELECT AgeGroup, COUNT(*) AS total_count FROM datasetb GROUP BY AgeGroup ORDER BY AgeGroup''')
	
	result = cur.fetchall()
	
	AgeGroup = []
	AgeGroup_Count = []

	for values in result:
		#print(values["AgeGroup"], values["total_count"])
		AgeGroup.append(values["AgeGroup"])
		AgeGroup_Count.append(values["total_count"])
	print(AgeGroup_Count)

	return render_template('datasetb.html', labels = AgeGroup, data = AgeGroup_Count)

if __name__ == "__main__":
    app.run(debug=True)

app.run()

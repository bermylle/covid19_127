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
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
app.config['MYSQL_DB'] = ''
app.config['MYSQL_CURSORCLASS'] = '' 
# app.config['MYSQL_USER'] = ''
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_DB'] = ''
# app.config['MYSQL_CURSORCLASS'] = '' 
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

	# [Age Group]
	cur = mysql.connection.cursor()
	cur.execute('''SELECT AgeGroup, COUNT(*) AS total_count FROM datasetb GROUP BY AgeGroup ORDER BY AgeGroup DESC''')
	result = cur.fetchall()
	
	AgeGroup = []
	AgeGroup_Count = []

	for values in result:
		AgeGroup.append(values["AgeGroup"])
		AgeGroup_Count.append(values["total_count"])

	# [Sex]
	cur_sex = mysql.connection.cursor()
	cur_sex.execute('''SELECT Sex, COUNT(*) AS total_count FROM datasetb GROUP BY Sex;''')
	result_sex = cur_sex.fetchall()

	sex_data = []
	sex_data_count = []

	for values in result_sex:
		sex_data.append(values["Sex"])
		sex_data_count.append(values["total_count"])


	# [RegProvRes]
	cur_rpr = mysql.connection.cursor()
	cur_rpr.execute('''SELECT DISTINCT (RegProvRes), COUNT(*) AS total_count FROM datasetb GROUP BY RegProvRes ORDER BY total_count''')
	result_rpr = cur_rpr.fetchall()

	rpr_data = []
	rpr_data_count = []

	for values in result_rpr:
		rpr_data.append(values["RegProvRes"])
		rpr_data_count.append(values["total_count"])

	# [MuniCityRes]
	cur_mcr = mysql.connection.cursor()
	cur_mcr.execute('''SELECT DISTINCT (MuniCityRes), COUNT(*) AS total_count FROM datasetb GROUP BY MuniCityRes ORDER BY total_count''')
	result_mcr = cur_mcr.fetchall()

	mcr_data = []
	mcr_data_count = []

	for values in result_mcr:
		mcr_data.append(values["MuniCityRes"])
		mcr_data_count.append(values["total_count"])

	# TABLE
	cur_table = mysql.connection.cursor()
	cur_table.execute(''' SELECT * FROM datasetb''')
	result_table = cur_table.fetchall()

	return render_template('datasetb.html', labels = AgeGroup, 
		data = AgeGroup_Count ,labels_sex = sex_data, data_sex = sex_data_count, 
		labels_rpr = rpr_data, data_rpr = rpr_data_count, 
		labels_mcr = mcr_data, data_mcr = mcr_data_count, data_table = result_table)

if __name__ == "__main__":
    app.run(debug=True)

app.run()

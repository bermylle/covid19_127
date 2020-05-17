import flask
from flask import render_template


from datasets.ph_data import *
from datasets.ind_data import *
from datasets.sgp_data import *
from datasets.mys_data import *
from datasets.prk_data import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
@app.route('/home')
def index():
	return render_template('dashboard.html')


@app.route('/graphs')
def graphs():
	return render_template('graphs.html', ph_confirmed = ph_confirmed, 
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

 
if __name__ == "__main__":
    app.run(debug=True)

app.run()

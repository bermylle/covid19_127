import flask
from flask import render_template
import urllib.request, json 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


with urllib.request.urlopen("https://pomber.github.io/covid19/timeseries.json") as url:
	data_world = json.loads(url.read().decode()) # dict
print(data_world["Philippines"][-1])
# print(type(data_world))

# DATA SETS
ph_data = data_world["Philippines"] # SAMPLE : {'date': '2020-5-15', 'confirmed': 12091, 'deaths': 806, 'recovered': 2460}

ph_dates = []
ph_confirmed = []
ph_recoveries = []
ph_deaths = []

for values in ph_data:
	if values["confirmed"] > 100:
		#print(values["confirmed"])
		ph_dates.append(values["date"])

for values in ph_data:
	if values["confirmed"] > 100:
		#print(values["confirmed"])
		ph_confirmed.append(values["confirmed"])

for values in ph_data:
	if values["confirmed"] > 100:
		#print(values["confirmed"])
		ph_recoveries.append(values["recovered"])


for values in ph_data:
	if values["confirmed"] > 100:
		#print(values["confirmed"])
		ph_deaths.append(values["deaths"])


peru = data_world["Peru"]
chn = data_world["China"]
fn = data_world["France"]
ita = data_world["Italy"]


@app.route('/')
@app.route('/home')
def index():
	return render_template('dashboard.html')


@app.route('/graphs')
def linegraph():
	return render_template('linegraph.html', ph_confirmed = ph_confirmed, 
		ph_recoveries = ph_recoveries, ph_deaths = ph_deaths, ph_dates = ph_dates)

 
if __name__ == "__main__":
    app.run(debug=True)

app.run()

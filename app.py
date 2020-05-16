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

# lists
ph = data_world["Philippines"] # SAMPLE : {'date': '2020-5-15', 'confirmed': 12091, 'deaths': 806, 'recovered': 2460}
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
	return render_template('linegraph.html', ph = data_world)

 
if __name__ == "__main__":
    app.run(debug=True)

app.run()

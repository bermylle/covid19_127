from datasets.world_data import data_world

# DATA SETS FOR PH
mys_data = data_world["Malaysia"] # SAMPLE DATA : {'date': '2020-5-15', 'confirmed': 12091, 'deaths': 806, 'recovered': 2460}

mys_dates = mys_data[-1]["date"]
mys_confirmed_total = mys_data[-1]["confirmed"]
mys_recoveries_total = mys_data[-1]["recovered"]
mys_deaths_total = mys_data[-1]["deaths"]
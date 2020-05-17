from datasets.world_data import data_world

# DATA SETS FOR PH
sgp_data = data_world["Singapore"] # SAMPLE DATA : {'date': '2020-5-15', 'confirmed': 12091, 'deaths': 806, 'recovered': 2460}

sgp_dates = sgp_data[-1]["date"]
sgp_confirmed_total = sgp_data[-1]["confirmed"]
sgp_recoveries_total = sgp_data[-1]["recovered"]
sgp_deaths_total = sgp_data[-1]["deaths"]


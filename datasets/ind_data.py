from datasets.world_data import data_world

# DATA SETS FOR PH
ind_data = data_world["Indonesia"] # SAMPLE DATA : {'date': '2020-5-15', 'confirmed': 12091, 'deaths': 806, 'recovered': 2460}

ind_dates = ind_data[-1]["date"]
ind_confirmed_total = ind_data[-1]["confirmed"]
ind_recoveries_total = ind_data[-1]["recovered"]
ind_deaths_total = ind_data[-1]["deaths"]

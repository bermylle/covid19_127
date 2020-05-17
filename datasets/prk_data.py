from datasets.world_data import data_world

# DATA SETS FOR PH
prk_data = data_world["Korea, South"] # SAMPLE DATA : {'date': '2020-5-15', 'confirmed': 12091, 'deaths': 806, 'recovered': 2460}

prk_dates = prk_data[-1]["date"]
prk_confirmed_total = prk_data[-1]["confirmed"]
prk_recoveries_total = prk_data[-1]["recovered"]
prk_deaths_total = prk_data[-1]["deaths"]
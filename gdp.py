import pandas as pd

def convert_numeric(value):
	if isinstance(value, int):
		return float(value)
	elif 'k' in value:
		return float(value.replace('k', '')) * 1000
	else:
		return float(value)

gdp_data = pd.read_csv('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
print(gdp_data.head())

## modify all columns to get actual numbers
column_list = gdp_data.columns.to_list()[1::]
for column in column_list:
	gdp_data[column] = gdp_data[column].apply(convert_numeric)

## Average mean for Colombia between 2015 and 2021
gdp_data.set_index('country', inplace = True)

years = [str(year) for year in range(2015, 2022, 1)]
avg_gdp_colombia = gdp_data.query('country == "Colombia"')[years].mean(axis = 1)

print (f'gdp_colombia {avg_gdp_colombia}') 



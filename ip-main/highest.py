import pandas as pd

# Create a Series with the data
data = {'Uttar Pradesh': 52.32, 'Tamil Nadu': 45.39, 'Jharkhand': 41.68}
adulteration_rates = pd.Series(data)

print(adulteration_rates)

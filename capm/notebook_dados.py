# The overall objective of this section is to check if the return observed
# applying the Magic Formula is due to the strategy or due to the risk taken.

import pandas as pd

from pathlib import Path

# Mostrar floats com duas casas decimas
pd.set_option("display.float_format", lambda x: "%.3g" % x)
pd.options.display.max_colwidth = 20
pd.options.display.max_columns = 20
pd.options.display.max_rows = 6

# Here we will load the data from the magic formula section.
# The first dataframe contains the prices of the assets.
df_prices = pd.read_csv("./data/3_prices.csv", parse_dates=["cutoff_date"])
df_prices

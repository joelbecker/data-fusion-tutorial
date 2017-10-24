import pandas as pd
import helpers as h

h.pandas_setup()

scraped_df = pd.DataFrame.from_csv('fusion-script/data/scraped/scraped-universities-subset.csv')
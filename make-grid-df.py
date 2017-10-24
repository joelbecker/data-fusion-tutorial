import pandas as pd
import helpers as h

h.pandas_setup()

grid_base = pd.DataFrame.from_csv('./data/grid20170926/grid-subset.csv')

grid_inst = pd.DataFrame.from_csv('./data/grid20170926/institutes.csv')
grid_inst = grid_inst[['established']]

grid_df = grid_base.join(grid_inst)

grid_df.to_csv('./data/grid-df.csv')
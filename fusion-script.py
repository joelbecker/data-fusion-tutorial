import pandas as pd
import recordlinkage as rl
import helpers as h

h.pandas_setup()

df_a = pd.DataFrame.from_csv('./data/grid-df.csv').reset_index()
df_b = pd.DataFrame.from_csv('./data/scraped/scraped-universities-subset.csv').reset_index()

indexer = rl.FullIndex()
candidate_links = indexer.index(df_a, df_b)

comp = rl.Compare(candidate_links, df_a, df_b)
comp.string('grid-name', 'scraped-name')

preds = [(1 if i >= .9 else 0) for i in comp.vectors[0]]

fuse = rl.FuseLinks()


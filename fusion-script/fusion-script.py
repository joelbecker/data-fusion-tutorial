import pandas as pd
import recordlinkage as rl

# Fuse GRID institutions with messy web scraped institutions.
# A good case study for

df_a = pd.DataFrame()
df_b = pd.DataFrame()

indexer = rl.FullIndex()
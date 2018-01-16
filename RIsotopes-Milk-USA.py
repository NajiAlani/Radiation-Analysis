import numpy as np
import pandas as pd

data = 'C:/Users/soso/Desktop/Projects/GitHub Projects/DS/Radiation-Analysis/Milk_RadNet_Lab_Analysis.csv'
df = pd.read_csv(data)
rad = df.replace({'Non-detect': np.nan})

isot_complete = rad[['Ba-140', 'Co-60', 'Cs-134', 'Cs-136', 'Cs-137', 'I-131', 'I-132', 'I-133', 'Te-129', 'Te-129m', 'Te-132']]
isot_reduce_row_all_NaN = isot_complete.dropna(how='all')
isot_reduce_col_all_NaN = isot_reduce_row_all_NaN.dropna(how='all', axis=1)
isot = isot_reduce_col_all_NaN
info = df.ix[[25, 26, 28, 32, 34, 35, 38, 39, 40, 41, 56],['State', 'Location', 'Date Posted', 'Date Collected', 'Sample Type', 'Unit']]
isotopes = pd.concat([info, isot], axis=1)
print(isotopes)

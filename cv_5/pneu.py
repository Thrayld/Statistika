import pandas as pd
import scipy.stats as stats


df = pd.read_csv('ojetipneu.txt', delimiter=' +')
_, p_value = stats.ttest_rel(df['Leva'], df['Prava'], alternative='greater')
print(f'p-value: {p_value:.3f}')

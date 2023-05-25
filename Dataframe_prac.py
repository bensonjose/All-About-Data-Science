import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv(r"C:\Users\Bindu\Downloads\laliga_player_stats_english.csv")
print(df)
# print(df.describe())
# print(df.max())
# print(df.min())
# print(df.median())


profile=ProfileReport(df)
profile.to_file(output_file="laliga.html")

import pandas as pd

# Load data from CSV file
df = pd.read_csv('data/eu_death_cause.csv')

# Get reusable list values
country_list = df['Country'].unique()
year_list = df['Year'].unique()
cause_list = list(df.columns)[3:-2]

# Dataframe for considering numbers per milion
df_million = df.copy()
df_million[cause_list] = df_million[cause_list].apply(lambda x: round((x / df_million['Population']) * 1000000, 2))
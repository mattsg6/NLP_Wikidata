import sqlite3
import pandas as pd
import os
from os import listdir

# Create wikidata.db database
con = sqlite3.connect('./data/database/wikidata.db')

# Initialize db with schema
with open('./data/database/schema.sql') as f:
    con.executescript(f.read())

cur = con.cursor()

#### LOAD CREW DATA ####
# Get CSV file names
path = os.path.abspath(os.getcwd()) + '/data/wikidata_crew'
filenames = listdir(path)
files = [ filename for filename in filenames if filename.endswith( '.csv' ) ]

# Load CSV data into dataframe
crew_dfs = []

for f in files:
    df = pd.read_csv(path + '/' + f)
    crew_dfs.append(df)

crew_frame = pd.concat(crew_dfs, axis=0)
crew_frame = crew_frame.drop_duplicates()

crew_frame.to_sql('crew', con, if_exists='append', index=False)

#### LOAD FILM DATA ####
# Get CSV file names
path = os.path.abspath(os.getcwd()) + '/data/wikidata_film'

# Load CSV data into datafram
film_df = pd.read_csv(path + '/' + 'films.csv')
film_df = film_df.drop_duplicates()
film_df.to_sql('films', con, if_exists='append', index=False)

#### LOAD UTIL DATA ####
# Dictionary of utility IDs
util_ids = {
    'film director': 'Q2526255',
    'cinematographer': 'Q222344',
    'film producer': 'Q3282637',
    'film actor': 'Q10800557'
}

for u in util_ids:
    cur.execute(f"INSERT INTO util (wikidata_id, connector) VALUES ('{util_ids[u]}', '{u}')")

con.commit()
con.close()
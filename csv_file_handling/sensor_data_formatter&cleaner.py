#Sensor Data Formatter
#Read messy CSV sensor logs and clean them (remove nulls, fix timestamps).
#Learn: CSV, regex, data cleaning

import re
#import csv
import pandas as pd

#function to extract temperature as float
def extract_temp(x):
    if pd.isna(x):
        return None

    s = str(x).lower()
    match = re.search(r"[-+]?\d*\.?\d+", s)

    if match:
        return float(match.group())
    return None

with open("sectionA_problem1_messy_sensor_logs.csv") as csvfile:
    #csv1 = csv.DictReader(csvfile, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    # rows = list(csv1)
    df = pd.read_csv(csvfile)
    for i,row in df.iterrows():
        print(f"{row['timestamp']}                    {row['temp_C']}")

    #removing null values
    new_df = df.dropna().copy()#new_df was just a filtered view...we need to copy
    print("\n CLEANED DATA ")
    print(new_df)
    new_df.to_csv("cleaned_data.csv", index=False)

    #converting temperature from strings to float using regex
    #using apply function we can apply one function to the whole column
    new_df['temp_C'] = new_df['temp_C'].apply(extract_temp)

    #fixing some of the data
    new_df['temp_C'] = (new_df['temp_C']*9/5)+32

    df.to_csv("cleaned_data.csv", index=False)

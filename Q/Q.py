#Sensor Data Formatter
#Read messy CSV sensor logs and clean them (remove nulls, fix timestamps).
#Learn: CSV, regex, data cleaning

import re
import csv
import pandas as pd

with open("sectionA_problem1_messy_sensor_logs.csv") as csvfile:
    #csv1 = csv.DictReader(csvfile, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    # rows = list(csv1)
    df = pd.read_csv(csvfile)
    for i,row in df.iterrows():
        print(f"{row['timestamp']}                    {row['temp_C']}")

    #removing null values
    new_df = df.dropna()
    print("\n CLEANED DATA ")
    print(new_df)
    new_df.to_csv("cleaned_data.csv", index=False)

    #converting temperature from strings to float using regex


    #fixing some of the data
    new_df['temp_C'] = (new_df['temp_C']*9/5)+32


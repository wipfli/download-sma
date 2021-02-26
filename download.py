import requests
import pandas as pd
import io
import datetime
import math
import influxdb
import time


def get_sma_to_wigos():
    sma_to_wigos = {}
    r = requests.get('https://data.geo.admin.ch/ch.meteoschweiz.messnetz-automatisch/ch.meteoschweiz.messnetz-automatisch_de.csv')
    df = pd.read_csv(io.StringIO(r.text), sep=';', na_values='-')
    for i in range(299):
        if df.loc[i]['Stationstyp'] == 'Wetterstation':
            wigos = df.loc[i]['WIGOS-ID']
            sma = df.loc[i]['Abk.']
            sma_to_wigos[sma] = wigos
    return sma_to_wigos

def get_data():
    r = requests.get('https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv')
    df = pd.read_csv(io.StringIO(r.text), sep=';', na_values='-')
    return df

def get_timestamp(df):
    return df['Date'][0]

def get_points(df):
    points = []
    timestamp = get_timestamp(df)
    influx_time = datetime.datetime.strptime(str(timestamp), 
        '%Y%m%d%H%M').strftime('%Y-%m-%dT%H:%M:%SZ')
    sma_to_wigos = get_sma_to_wigos()
    for i in range(len(df['Date'])):
        for col in df.columns.values[2:]:
            value = float(df[col][i])
            if not math.isnan(value):
                point = {
                    'measurement': 'stations',
                    'tags': {
                        'id': sma_to_wigos[df['Station/Location'][i]],
                        'key': col
                    }, 
                    'fields': {
                        'value': value
                    },
                    'time': influx_time
                }
                points += [point]
    return points

def save(points):
    client = influxdb.InfluxDBClient(database='weather')
    client.write_points(points)


if __name__ == '__main__':
    last_timestamp = ''
    while True:
        df = get_data()
        timestamp = get_timestamp(df)
        if timestamp != last_timestamp:
            last_timestamp = timestamp
            points = get_points(df)
            save(points)
        time.sleep(10)
import wget
import pandas
from flask import Flask
import logging
import os


def download():
    url='https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv'
    #wget.download(url)
    csv=pandas.read_csv('TAM_MMM_TpsReel.csv',sep=';')
    return csv
#print(download)

def stations():
    df=download()
    stations=set(df['stop_name'].tolist())
    return stations
print(stations())

def city_station():
    df=download()
    stations=set(df['stop_name''departure_time'].tolist())
    return city_station
print(city_station())

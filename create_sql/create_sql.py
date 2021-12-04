import yfinance as yf
import os
import pandas as pd
import datetime
from flask_sqlalchemy import sqlalchemy

start = datetime.datetime(2014,1,1)
end = datetime.datetime(2021,12,3)

def make_list():

    f = open(r"global500.txt", "r")
    symbols = []
    companies = []
    for line in f:
        line = line[:-1]
        symbol, company = line.split(";")
        symbols.append(symbol)
        companies.append(company)

    return symbols, companies

def getdata(tickers):

    data = []
    for ticker in tickers:
        data.append(yf.download(ticker,start=start,end=end).reset_index())
    return data

def createengine(name):
    engine = sqlalchemy.create_engine('sqlite:///'+name)
    return engine

def TOSQL(frames,symbols,engine):
    for frame,symbol in zip(frames,symbols):
        frame.to_sql(symbol, engine, index=False)
    print('Successfully imported data')
    

symbols , companies = make_list()

TOP= getdata(symbols)
TOP_engine=createengine('TOP')

TOSQL(TOP,symbols,TOP_engine)
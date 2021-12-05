import yfinance as yf
import os
import plotly.graph_objects as go
import datetime
from flask_sqlalchemy import sqlalchemy
import sqlite3

start = datetime.datetime(2014,1,1)
end = datetime.datetime(2021,12,3)

def make_plot(id, company):
    
    #connection = sqlite3.connect('data/TOP.db')
    #cursor = connection.cursor()
    #vect = []

    #for row in cursor.execute(f"SELECT Date,Close FROM {id}"):
    #    vect.append(row)
   

    #fig = go.Figure(data =[go.Scatter(vect)])
    
    tickerData = yf.Ticker(id)
    tickerDf = tickerData.history(
        period='1d', start='2014-1-1', end='2021-12-4')

    a = datetime.datetime.today()
    numdays = 2895
    dateList = []
    for x in range(numdays, 0, -2):
        dateList.append(a - datetime.timedelta(days=x))

    fig = go.Figure(data =[go.Scatter(x=dateList, y=tickerDf['Close'])])
    fig.update_layout(title_text=f"{company}",font_color="#000000",font_size=25,title_x=0.5,xaxis_title="Date",
    yaxis_title="Dollars")

    fig.write_html(f"data/templates/{company}.html")


def make_list():

    f = open(r"data/global500.txt", "r", errors='ignore')
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

def TOSQL(frames,symbols,engine):
    for frame,symbol in zip(frames,symbols):
        frame.to_sql(symbol, engine, index=False)
    print('Successfully imported data')
   
def createengine(name):
    engine = sqlalchemy.create_engine('sqlite:///'+name+'.db')
    return engine

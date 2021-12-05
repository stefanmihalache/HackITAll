from datetime import datetime
from flask import render_template
from data import app
from data.functions import *
import os
from flask import request
from flask_sqlalchemy import sqlalchemy


symbols , companies = make_list()
n = len(symbols)

#creare baza de date
#TOP= getdata(symbols)
#TOP_engine=createengine('TOP')
#TOSQL(TOP,symbols,TOP_engine)


@app.route('/')
def home():
    
    return render_template(
        "front.html")

@app.route('/search')

def company():
    name = request.args.get('search')
    i=0
    for i in range(n):
        if name == companies[i]: 
            break

    ok=0
    
    for file in os.listdir("data/templates"):
        if file.endswith(f"{name}.html"):
            ok =1
            break

    if ok == 0:
        make_plot(symbols[i],name)
    
    return render_template(
        f"{name}.html")

